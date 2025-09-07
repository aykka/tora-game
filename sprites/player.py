from config import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path_r, image_path_l):
        super().__init__()
        self.image_right = pygame.image.load(image_path_r).convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (SQUARE_SIZE,SQUARE_SIZE))
        self.image_left = pygame.image.load(image_path_l).convert_alpha()
        self.image_left = pygame.transform.scale(self.image_left, (SQUARE_SIZE,SQUARE_SIZE))
        self.image = self.image_right

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  

    def update(self, keys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_img = pygame.image.load('Assets/Tora_left.png').convert_alpha()
            player_img = pygame.transform.scale(player_img, (SQUARE_SIZE,SQUARE_SIZE))
            self.move_left()
        elif keys[pygame.K_RIGHT]:
            player_img = pygame.image.load('Assets/Tora_right.png').convert_alpha()
            player_img = pygame.transform.scale(player_img, (SQUARE_SIZE,SQUARE_SIZE))
            self.move_right()

        self.apply_gravity()
        

    def set_position(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.rect.x = x
            self.rect.y = y
        else:
            raise ValueError('Incorrect argumets provided: must be an int')

    def get_position(self):
        return (self.rect.x, self.rect.y)
    
    def move_right(self):
        self.rect.x += SPEED
        self.image = self.image_right

    def move_left(self):
        if self.rect.x >= 0:
            self.rect.x -= SPEED
            self.image = self.image_left
    
    def jump(self):
        if round(self.rect.y) == GROUND_LVL:
            self.rect.y -= JUMP_HEIGHT
            
    def apply_gravity(self):
        if self.rect.y < GROUND_LVL:
            self.rect.y += GRAVITY # TODO: FIX GRAVITY
