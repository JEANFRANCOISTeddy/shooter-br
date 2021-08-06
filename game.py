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
        tmx_data = pytmx.util_pygame.load_pygame('./assets/maps/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # map_layer.zoom = 2

        self.player = Player.Player(400, 400, 6, 10)

        # Layers
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):
        # Game loop
        running = True

        # A container class to hold and manage multiple Sprite objects.
        # moving_sprites = pygame.sprite.Group()
        # player = Player.Player(400, 400, 6, 10)
        # moving_sprites.add(player)
        # player.update(player.get_speed())

        # Add range to user
        # player.set_range(50)
        # player.display_range(self.screen)
        # pygame.display.update()

        while running:
            # self.group.draw(self.screen)
            # pygame.display.flip()

            self.group.update(0.25)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    print("Window closed")
                    sys.exit()

            key_input = pygame.key.get_pressed()

            if key_input[pygame.K_RIGHT]:
                self.player.walk()
                self.player.walk_right()
            elif key_input[pygame.K_LEFT]:
                self.player.walk()
                self.player.walk_left()
            elif key_input[pygame.K_UP]:
                self.player.walk()
                self.player.walk_up()
            elif key_input[pygame.K_DOWN]:
                self.player.walk()
                self.player.walk_down()

            #self.group.update(0.25)
            #pygame.display.flip()
            # self.screen.fill((255, 255, 255))
            # moving_sprites.draw(self.screen)
            # moving_sprites.update(0.25)
            # pygame.display.flip()
            clock.tick(30)

        pygame.quit()
