import pygame
import pytmx
import pyscroll


class Game:

    def __init__(self):

        # Game screen
        self.screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Shooter Br")

        # Map (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRendered(map_data, self.screen.get_size())

        # Layers
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):

        # Game loop
        running = True

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()
