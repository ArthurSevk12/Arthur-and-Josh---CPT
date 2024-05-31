import pygame
from Button import Button
from GameBoard import board_draw


def draw_how_2_play_menu():
    # The bottom two lines load the png images for the buttons
    board_image = pygame.image.load('How_To_Play_Menu.png').convert_alpha()
    start_img = pygame.image.load('START_button.png').convert_alpha()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic-Tac-Toe!")

    start_button = Button(300, 430, start_img)

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

        # This calls the game board menu
        if start_button.draw(screen):
            done = True
            board_draw()

        # Update the screen with drawing.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()
