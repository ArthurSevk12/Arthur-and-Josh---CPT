import pygame


def board_draw():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SAND = (225, 198, 153)

    board_image = pygame.image.load('Gameboard.png').convert_alpha()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic-Tac-Toe!")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.blit(board_image, (0, 0))

        # Update the screen with drawing.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


class Board:
    pass
