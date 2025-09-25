import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color = (168, 117, 50)
        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, keys):
        pass 