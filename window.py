import pygame

pygame.init()

display_width = 1000
display_height = 800

pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Shooter Br")

icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(icon)

running = True
#pd
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Window closed")