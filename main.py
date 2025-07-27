import pygame
from config import *
from player import Player
from coin import Coin

pygame.init()
running = True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

Tora = Player(0, GROUND_LVL, 'Assets/Tora_right.png')
Shora = Player(0, GROUND_LVL, 'Assets/Tora_left.png')

player_img = pygame.image.load('Assets/Tora_right.png').convert_alpha()
player_img = pygame.transform.scale(player_img, (SQUARE_SIZE,SQUARE_SIZE))

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
    if keys[pygame.K_LEFT]:
        player_img = pygame.image.load('Assets/Tora_left.png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (SQUARE_SIZE,SQUARE_SIZE))
        Tora.move_left()
    elif keys[pygame.K_RIGHT]:
        player_img = pygame.image.load('Assets/Tora_right.png').convert_alpha()
        player_img = pygame.transform.scale(player_img, (SQUARE_SIZE,SQUARE_SIZE))
        Tora.move_right()

    Tora.apply_gravity()
        
    # Draw the square   
    screen.blit(player_img,(Tora.x, Tora.y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.circle(screen, coin.color, (coin.x, coin.y), coin.radius)

    
    pygame.display.flip()
pygame.quit()
