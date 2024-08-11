import pygame
import random

pygame.init()

# Ventana
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Game")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Jugador
player_width = 65
player_height = 65
player = pygame.Rect(WIDTH // 2 - player_width // 2,
                     HEIGHT - player_height - 10, player_width, player_height)

#images
player_img = pygame.image.load("pomni.png").convert_alpha()
bubble_img = pygame.image.load("bubble.png").convert_alpha()
background_img = pygame.image.load("circus.jpeg")

#dimensions
player_size = (80, 80)
meteor_size = (50, 50)

player_img = pygame.transform.scale(player_img, player_size)
bubble_img = pygame.transform.scale(bubble_img, meteor_size)



#Meteor

meteor_width = 30
meteor_height = 30
meteors = []

#scores
score = 0
font = pygame.font.Font(None, 35)


# Tiempo del juego
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5

    #Generar meteors
    if len(meteors) < 8:
        meteor = pygame.Rect(random.randint(0, WIDTH - meteor_width),
                             0, meteor_width, meteor_height)
        meteors.append(meteor)
    for meteor in meteors:
        meteor.y += 5
        if meteor.top > HEIGHT:
            meteors.remove(meteor)
            score += 1


    # detection crush
    for meteor in meteors:
        if player.colliderect(meteor):
            running = False


    # Dibujar en pantalla
    screen.fill(BLACK)
    screen.blit(background_img, (0, 0))
    #pygame.draw.rect(screen, WHITE, player)
    screen.blit(player_img, player)
    for meteor in meteors:
        screen.blit(bubble_img, meteor)
        #pygame.draw.rect(screen, RED, meteor)

    #Show scores
    score_text = font.render(f"Puntos: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
