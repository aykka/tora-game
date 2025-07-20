import pygame
from config import MAIN_COLOR, WIDTH, HEIGHT, CAPTION, SQUARE_SIZE, COLOR
from player import Player

pygame.init()
running = True


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)

Tora = Player(0, HEIGHT-SQUARE_SIZE)

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
        Tora.move_left()
    elif keys[pygame.K_RIGHT]:
        Tora.move_right()
        
    # Draw the square   
    pygame.draw.rect(screen, COLOR, (Tora.x, Tora.y, SQUARE_SIZE, SQUARE_SIZE))

    
    pygame.display.flip()
pygame.quit()


