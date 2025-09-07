import pygame
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        print(x, y)
        self.color = (255, 215, 0)
        self.radius = 10
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        pygame.draw.circle(self.image, self.color, (x, y), self.radius)
        self.rect = self.image.get_rect(center=(x, y))
    
    def update(self, keys):
        pass 