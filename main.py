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

Player_Group = pygame.sprite.Group()
Other_Group = pygame.sprite.Group()

sprites = getLevel('./levels/1.txt')
for sprite in sprites:
    Other_Group.add(sprite)


Player_Group.add(Tora)


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

    Other_Group.update()
    Other_Group.draw(screen)

    Player_Group.update(keys)
    Player_Group.draw(screen)
        
    
    
    pygame.display.flip()
pygame.quit()

