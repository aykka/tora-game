import pygame
from config import *
from sprites.player import Player
from sprites.coin import Coin
from utils.level import getLevel


pygame.init()
running = True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

Tora = Player(0, GROUND_LVL, 'Assets/Tora_right.png', 'Assets/Tora_left.png')

all_sprites = pygame.sprite.Group()
all_sprites.add(Tora)

sprites = getLevel('./levels/1.txt')
for sprite in sprites:
    all_sprites.add(sprite)


while running:
    screen.fill(MAIN_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Single key press 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Tora.jump()

    # Key hold
    keys = pygame.key.get_pressed()
    all_sprites.update(keys)

    all_sprites.draw(screen)
        
    
    
    pygame.display.flip()
pygame.quit()

