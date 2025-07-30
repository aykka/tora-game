import pygame
from config import *
from player import Player
from coin import Coin

pygame.init()
running = True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

Tora = Player(0, GROUND_LVL, 'Assets/Tora_right.png', 'Assets/Tora_left.png')
Shora = Player(0, GROUND_LVL, 'Assets/Tora_left.png', 'Assets/Tora_right.png')

all_sprites = pygame.sprite.Group()
all_sprites.add(Tora)

coin = Coin(302, GROUND_LVL-15)

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
        
    # Draw the square   

    pygame.draw.circle(screen, coin.color, (coin.x, coin.y), coin.radius)

    
    pygame.display.flip()
pygame.quit()

