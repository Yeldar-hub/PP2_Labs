import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Crazy Paint by Yeldar")
    clock = pygame.time.Clock()
    
    radius = 10
    x = 0
    y = 0
    mode = 'draw'  
    color = (255, 255, 255)  
    start_pos = None
    drawing = False
    points = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_d:
                    mode = 'draw'
                elif event.key == pygame.K_r:
                    mode = 'rect'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    mode = 'erase'
                
                # --- Color selection ---
                elif event.key == pygame.K_1:
                    color = (255, 0, 0)  # Red
                elif event.key == pygame.K_2:
                    color = (0, 255, 0)  # Green
                elif event.key == pygame.K_3:
                    color = (0, 0, 255)  # Blue
                elif event.key == pygame.K_4:
                    color = (255, 255, 0)  # Yellow
                elif event.key == pygame.K_5:
                    color = (255, 255, 255)  # White
                elif event.key == pygame.K_6:
                    color = (0, 0, 0)  # Black

            # --- Mouse control ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                elif event.button == 3:  # Right click
                    radius = max(1, radius - 1)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    end_pos = event.pos
                    if mode == 'rect':
                        draw_rect(screen, start_pos, end_pos, color, radius)
                    elif mode == 'circle':
                        draw_circle_shape(screen, start_pos, end_pos, color, radius)
                    drawing = False

            elif event.type == pygame.MOUSEMOTION and drawing:
                position = event.pos
                if mode == 'draw':
                    pygame.draw.circle(screen, color, position, radius)
                elif mode == 'erase':
                    pygame.draw.circle(screen, (0, 0, 0), position, radius)

        pygame.display.set_caption(f"Mode: {mode.upper()} | Color: {color} | Brush Size: {radius}")
        pygame.display.flip()
        clock.tick(60)


def draw_rect(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                       abs(x2 - x1), abs(y2 - y1))
    pygame.draw.rect(screen, color, rect, width)

def draw_circle_shape(screen, start, end, color, width):
    x1, y1 = start
    x2, y2 = end
    radius = int(((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius, width)

main()
