import pygame
import sys
import pytmx
import pyscroll

from classes import Player

clock = pygame.time.Clock()


class Game:

    def __init__(self, display_width, display_height):
        # Game screen
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Shooter Br")
        icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(icon)

        # Map (tmx)
        # tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        # map_data = pyscroll.data.TiledMapData(tmx_data)
        # map_layer = pyscroll.orthographic.BufferedRendered(map_data, self.screen.get_size())

        # Layers
        # self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        # Game loop
        running = True

        # A container class to hold and manage multiple Sprite objects.
        moving_sprites = pygame.sprite.Group()
        player = Player.Player(400, 400)
        moving_sprites.add(player)

        while running:

            # self.group.draw(self.screen)
            # pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Window closed")
                    sys.exit()

            key_input = pygame.key.get_pressed()

            if key_input[pygame.K_RIGHT]:
                player.walk()
            elif key_input[pygame.K_LEFT]:
                player.walk()
            elif key_input[pygame.K_UP]:
                player.walk()
            elif key_input[pygame.K_DOWN]:
                player.walk()

            self.screen.fill((255, 255, 255))
            moving_sprites.draw(self.screen)
            moving_sprites.update(0.25)
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
