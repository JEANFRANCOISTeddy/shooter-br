import pygame
from game import Game

# Game screen
display_width = 1000
display_height = 800

if __name__ == '__main__':
    pygame.init()
    game = Game(display_width, display_height)
    game.run()
