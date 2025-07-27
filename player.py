from config import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SQUARE_SIZE,SQUARE_SIZE))
        self.image_path = image_path

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  

    def update(self):
        pass

    def set_position(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise ValueError('Incorrect argumets provided: must be an int')

    def get_position(self):
        return (self.x, self.y)
    
    def move_right(self):
        self.x += SPEED

    def move_left(self):
        if self.x >= 0:
            self.x -= SPEED
    
    def jump(self):
        if round(self.y) == GROUND_LVL:
            self.y -= JUMP_HEIGHT
            
    def apply_gravity(self):
        if self.y < GROUND_LVL:
            self.y += GRAVITY
