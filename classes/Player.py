import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.walk_animation = False
        self.sprites = []

        self.load_assets('walk_right_')
        self.load_assets('walk_left_')
        self.load_assets('walk_up_')
        self.load_assets('walk_down_')

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def load_assets(self, path):
        for i in range(4):
            new_path = path + str(i+1)
            picture = pygame.image.load('./assets/character/' + new_path + '.png')
            picture = pygame.transform.scale2x(picture)
            self.sprites.append(picture)

    def walk(self):
        self.walk_animation = True

    def update(self, speed):
        if self.walk_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk_animation = False

        self.image = self.sprites[int(self.current_sprite)]
