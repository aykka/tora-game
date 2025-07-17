import pygame

pygame.init()
running = True
MAIN_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((1400, 1000))
pygame.display.set_caption("Tora")

while running:
    screen.fill(MAIN_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # # Draw the square
    # pygame.draw.rect(screen, game_state['current_color'], (position['x'], position['y'], SQUARE_SIZE, SQUARE_SIZE))
    # pygame.draw.rect(screen, RED, (100, 300, SQUARE_SIZE, SQUARE_SIZE))
    # pygame.draw.circle(screen, current_color, )
    # Update the display
    pygame.display.flip()
pygame.quit()
