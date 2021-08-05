import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()
        self.walk_animation = False
        self.sprites = []
        self.load_assets('walk_right_', 2)
        self.load_assets('walk_left_', 2)
        self.load_assets('walk_up_', 2)
        self.load_assets('walk_down_', 2)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.position = [pos_x, pos_y]
        self.speed = speed

    def load_assets(self, path, scale):
        for i in range(4):
            new_path = path + str(i+1)
            picture = pygame.image.load('./assets/character/' + new_path + '.png')
            picture = pygame.transform.scale(picture, (int(picture.get_width() * scale), picture.get_height() * scale))
            self.sprites.append(picture)

    def walk(self):
        self.walk_animation = True

    def walk_right(self):
        self.position[0] += self.speed

    def walk_left(self):
        self.position[0] -= self.speed

    def walk_up(self):
        self.position[1] -= self.speed

    def walk_down(self):
        self.position[1] += self.speed

    def update(self, speed):
        if self.walk_animation:
            self.current_sprite += speed
            self.rect.topleft = self.position
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.walk_animation = False

        self.image = self.sprites[int(self.current_sprite)]

