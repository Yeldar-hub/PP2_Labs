import pygame
import random
import sys
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game from Yeldar")

# Colours 
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("Verdana", 20)

# Snake's initials
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
change_to = direction

# Def for food generation
def generate_food():
    while True:
        food_x = random.randrange(0, WIDTH - CELL_SIZE, CELL_SIZE)
        food_y = random.randrange(0, HEIGHT - CELL_SIZE, CELL_SIZE)
        # to not generate food on the my snake
        if (food_x, food_y) not in snake:
            return (food_x, food_y)
        
food = generate_food()

# Game things
score = 0
level = 1
speed = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
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
    
    # Checking if you стукнулся to border
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        print("Game Over!")
        pygame.quit()
        sys.exit()
    
    # Checking if you стукнулся to yourself
    if new_head in snake[1:]:
        print("Game Over!")
        pygame.quit()
        sys.exit()
    
    # Eating a food: grow or not grow
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 3 == 0:
            level += 1
            speed += 2  
    else:
        snake.pop()

    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (500, 10))

    pygame.display.flip()
    clock.tick(speed)  
