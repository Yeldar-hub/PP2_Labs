import pygame
import datetime

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Micky Clock")

micky = pygame.image.load("base_micky.jpg").convert()
micky = pygame.transform.scale(micky, (WIDTH, HEIGHT))

micky_left_hand = pygame.image.load("minute.png").convert_alpha()   
micky_right_hand = pygame.image.load("second.png").convert_alpha()  

scale_factor = 0.60  
micky_left_hand = pygame.transform.scale(
    micky_left_hand,
    (int(micky_left_hand.get_width() * scale_factor),
     int(micky_left_hand.get_height() * scale_factor))
)
micky_right_hand = pygame.transform.scale(
    micky_right_hand,
    (int(micky_right_hand.get_width() * scale_factor),
     int(micky_right_hand.get_height() * scale_factor))
)

center = (WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()
running = True

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    millisecond = now.microsecond / 1_000_000

    sec_angle = -6 * (second + millisecond)
    min_angle = -6 * (minute + second / 60)

    rotated_minute = pygame.transform.rotate(micky_left_hand, min_angle)
    rotated_second = pygame.transform.rotate(micky_right_hand, sec_angle)

    minute_rect = rotated_minute.get_rect(center=(center[0], center[1] + 15))
    second_rect = rotated_second.get_rect(center=(center[0], center[1] + 15))

    screen.fill((255, 255, 255))
    screen.blit(micky, (0, 0))
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
