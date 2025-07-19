import pygame
from config import MAIN_COLOR, SCREEN_SIZE, CAPTION

pygame.init()
running = True


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(CAPTION)

while running:
    screen.fill(MAIN_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # # Draw the square
    # pygame.draw.rect(screen, game_state['current_color'], (position['x'], position['y'], SQUARE_SIZE, SQUARE_SIZE))
    # pygame.draw.rect(screen, RED, (100, 300, SQUARE_SIZE, SQUARE_SIZE))
    # Update the display
    pygame.display.flip()
pygame.quit()
