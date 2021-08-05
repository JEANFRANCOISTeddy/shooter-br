import pygame
import sys
from classes import Player

pygame.init()
clock = pygame.time.Clock()

# Game screen
display_width = 1000
display_height = 800

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Shooter Br")

icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

running = True

# A container class to hold and manage multiple Sprite objects.
moving_sprites = pygame.sprite.Group()
player = Player.Player(400, 400)
moving_sprites.add(player)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Window closed")
            sys.exit()

    keyInput = pygame.key.get_pressed()

    if keyInput[pygame.K_RIGHT]:
        player.walk()
    elif keyInput[pygame.K_LEFT]:
        player.walk()
    elif keyInput[pygame.K_UP]:
        player.walk()
    elif keyInput[pygame.K_DOWN]:
        player.walk()

    screen.fill((255, 255, 255))
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
