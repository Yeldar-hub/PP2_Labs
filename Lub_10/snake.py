import time
import pygame
import random
import sys
import psycopg2
from config import load_config
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake by Yeldar")

# Colours
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
ORANGE  = (255, 165, 0)
GRAY    = (100, 100, 100)

font = pygame.font.SysFont("Verdana", 20)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
change_to = direction

FOOD_TYPES = [
    (RED, 1, 40),      # normal
    (ORANGE, 2, 30),   # medium
    (WHITE, 3, 20)     # rare
]

LEVELS = {
    1: {"speed": 5, "obstacles": 4},
    2: {"speed": 6, "obstacles": 6},
    3: {"speed": 7, "obstacles": 8},
    4: {"speed": 8, "obstacles": 10},
}

def generate_food(snake, obstacles):
    while True:
        food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
        food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
        pos = (food_x, food_y)
        if pos not in snake and pos not in obstacles:
            return pos

def new_food(snake, obstacles):
    color, value, life = random.choice(FOOD_TYPES)
    pos = generate_food(snake, obstacles)
    return {"pos": pos, "color": color, "value": value, "life": life}

def generate_obstacles(count, snake, food):
    obs = []
    while len(obs) < count:
        x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
        y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
        pos = (x, y)
        if pos not in snake and pos != food["pos"] and pos not in obs:
            obs.append(pos)
    return obs

# DATABASE 
def create_tables():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(50) UNIQUE NOT NULL
                    );
                """)
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS user_score (
                        user_id INTEGER PRIMARY KEY REFERENCES users(user_id) ON DELETE CASCADE,
                        level INTEGER DEFAULT 1,
                        score INTEGER DEFAULT 0,
                        snake_speed INTEGER DEFAULT 5
                    );
                """)
                conn.commit()
    except Exception as e:
        print("DB Error:", e)

def get_or_create_user(username):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT u.user_id, s.level, s.score, s.snake_speed
                    FROM users u LEFT JOIN user_score s ON u.user_id = s.user_id
                    WHERE username = %s;
                """, (username,))
                row = cur.fetchone()
                if row:
                    user_id, level, score, speed = row
                    if level is None:
                        level, score, speed = 1, 0, 5
                    print(f"Welcome back {username}! Level: {level}, Score: {score}")
                else:
                    cur.execute("INSERT INTO users(username) VALUES(%s) RETURNING user_id;", (username,))
                    user_id = cur.fetchone()[0]
                    level, score, speed = 1, 0, 5
                    cur.execute("INSERT INTO user_score(user_id, level, score, snake_speed) VALUES(%s, %s, %s, %s);",
                                (user_id, level, score, speed))
                    conn.commit()
                    print(f"New user {username} created! Level: {level}")
                return user_id, level, score, speed
    except Exception as e:
        print("DB Error:", e)
        return None, 1, 0, 5

def save_progress(user_id, score, level, speed):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE user_score
                    SET score = %s, level = %s, snake_speed = %s
                    WHERE user_id = %s;
                """, (score, level, speed, user_id))
                conn.commit()
                print(f"Progress saved: Level {level}, Score {score}")
    except Exception as e:
        print("Error saving progress:", e)

# ------------------- GAME START ---------------------
create_tables()
username = input("Enter your username: ")
user_id, level, score, speed = get_or_create_user(username)

food = new_food(snake, [])
obstacles = generate_obstacles(LEVELS[level]["obstacles"], snake, food)
last_obstacle_change = 0
paused = False

time.sleep(5)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            save_progress(user_id, score, level, speed)
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_progress(user_id, score, level, speed)
                    print("Game paused. Press P to resume.")

    if paused:
        pygame.time.delay(100)
        continue

    direction = change_to
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= CELL_SIZE
    elif direction == "DOWN":
        head_y += CELL_SIZE
    elif direction == "LEFT":
        head_x -= CELL_SIZE
    elif direction == "RIGHT":
        head_x += CELL_SIZE

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over! Hit wall.")
        save_progress(user_id, score, level, speed)
        pygame.quit()
        sys.exit()
    if new_head in snake[1:]:
        print("Game Over! Hit self.")
        save_progress(user_id, score, level, speed)
        pygame.quit()
        sys.exit()
    if new_head in obstacles:
        print("Game Over! Hit obstacle.")
        save_progress(user_id, score, level, speed)
        pygame.quit()
        sys.exit()

    food["life"] -= 1
    if new_head == food["pos"]:
        score += food["value"]
        if score % 3 == 0:  
            level = min(level + 1, max(LEVELS.keys()))
            speed = LEVELS[level]["speed"]
            obstacles = generate_obstacles(LEVELS[level]["obstacles"], snake, food)
        food = new_food(snake, obstacles)
    else:
        snake.pop()

    if food["life"] <= 0:
        food = new_food(snake, obstacles)

    current_tens = score // 10
    if current_tens > last_obstacle_change and score >= 10:
        obstacles = generate_obstacles(LEVELS[level]["obstacles"], snake, food)
        last_obstacle_change = current_tens

    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, food["color"], (food["pos"][0], food["pos"][1], CELL_SIZE, CELL_SIZE))
    for (ox, oy) in obstacles:
        pygame.draw.rect(screen, GRAY, (ox, oy, CELL_SIZE, CELL_SIZE))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.flip()
    clock.tick(speed)
