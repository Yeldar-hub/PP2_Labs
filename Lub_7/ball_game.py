import pygame

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball Movement")

RADIUS = 25
STEP = 20
x = WIDTH // 2
y = HEIGHT // 2

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                new_x = x - STEP
                if new_x - RADIUS >= 0:
                    x = new_x
            elif event.key == pygame.K_RIGHT:
                new_x = x + STEP
                if new_x + RADIUS <= WIDTH:
                    x = new_x
            elif event.key == pygame.K_UP:
                new_y = y - STEP
                if new_y - RADIUS >= 0:
                    y = new_y
            elif event.key == pygame.K_DOWN:
                new_y = y + STEP
                if new_y + RADIUS <= HEIGHT:
                    y = new_y

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()