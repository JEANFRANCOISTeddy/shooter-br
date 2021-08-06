import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, range):
        super().__init__()
        '''self.sprites = []
        self.load_assets('walk_right_', 2)
        self.load_assets('walk_left_', 2)
        self.load_assets('walk_up_', 2)
        self.load_assets('walk_down_', 2)
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]'''
        self.sprites = []
        self.image = pygame.image.load('./assets/character/no_walk.png')
        self.image.set_colorkey(255, 255)
        self.images = {
            'right': self.load_assets('walk_right_', 2),
            'left': self.load_assets('walk_left_', 2),
            'up': self.load_assets('walk_up_', 2),
            'down': self.load_assets('walk_down_', 2)

            #'right': pygame.image.load('./assets/character/walk_right_1.png'),
            #'left': pygame.image.load('./assets/character/walk_left_1.png'),
            #'up': pygame.image.load('./assets/character/walk_up_1.png'),
            #'down': pygame.image.load('./assets/character/walk_down_1.png')
        }
        self.current_sprite = 0

        self.walk_animation = False
        self.rect = self.image.get_rect()
        self.position = [pos_x, pos_y]
        self.speed = speed
        self.range = range

    def load_assets(self, path, scale):
        assets = []
        for i in range(4):
            new_path = path + str(i + 1)
            picture = pygame.image.load('./assets/character/' + new_path + '.png')
            picture = pygame.transform.scale(picture, (int(picture.get_width() * scale), picture.get_height() * scale))
            self.sprites.append(picture)
            assets.append(picture)
        return assets

    def change_direction(self, direction):
        self.current_sprite += self.get_speed()
        # 6                            4
        if int(self.current_sprite) >= len(self.images[direction]):
            self.current_sprite = 0
            self.walk_animation = False

        print(self.current_sprite)
        self.image = self.sprites[int(self.current_sprite)]

    def walk(self):
        self.walk_animation = True

    def walk_right(self):
        self.position[0] += self.get_speed()
        self.change_direction('right')

    def walk_left(self):
        self.position[0] -= self.get_speed()
        self.change_direction('left')

    def walk_up(self):
        self.position[1] -= self.get_speed()
        self.change_direction('up')

    def walk_down(self):
        self.position[1] += self.get_speed()
        self.change_direction('down')

    def display_range(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.position[0], self.position[1]), self.get_range())

    def update(self, speed):
        #if self.walk_animation:
            #self.current_sprite += speed
        self.rect.topleft = self.position
            #if int(self.current_sprite) >= len(self.sprites):
                #self.current_sprite = 0
                #self.walk_animation = False

        #self.image = self.sprites[int(self.current_sprite)]'''

    def set_range(self, range):
        self.range = range

    def get_range(self):
        return self.range

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed
