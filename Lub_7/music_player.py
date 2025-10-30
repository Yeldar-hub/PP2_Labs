import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Music from Yeldar")

current = 0
is_playing = False
songs = ["song_1.mp3", "song_2.mp3", "song_3.mp3"]
font = pygame.font.Font(None, 36)

pygame.mixer.music.load(songs[current])

done = False
while not done:
    screen.fill((200, 200, 255))

    text = font.render("Press P = Play, S = Stop, N = Next, B = Back", True, (0, 0, 0))
    screen.blit(text, (20, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
                is_playing = True
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            elif event.key == pygame.K_n:
                current += 1
                if current >= len(songs):
                    current = 0
                pygame.mixer.music.load(songs[current])
                if is_playing:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                current -= 1
                if current < 0:
                    current = len(songs) - 1
                pygame.mixer.music.load(songs[current])
                if is_playing:
                    pygame.mixer.music.play()
        
    pygame.display.update()

pygame.quit()

    