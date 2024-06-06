import pygame
from Icon import Icon

def board_draw():
    # Define some colors
    WHITE = (255, 255, 255)

    board_image = pygame.image.load('Gameboard.png').convert_alpha()
    arthurs_img = pygame.image.load('Arthurs_Face_CPT.png').convert_alpha()
    joshs_img = pygame.image.load('Joshuas_Face_CPT.png').convert_alpha()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic-Tac-Toe!")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    arthurs_face = Icon(arthurs_img)
    joshs_face = Icon(joshs_img)
    arthurs_positions = []  # List to store positions of icons
    joshs_positions = []

    user_turn = 1
    while not done:
        # --- Main event loop

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True

            if pygame.Rect(162, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 83))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((162, 83))
                    user_turn = 1

            elif pygame.Rect(290, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 83))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((290, 83))
                    user_turn = 1

            elif pygame.Rect(418, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 83))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((418, 83))
                    user_turn = 1

            elif pygame.Rect(162, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 195))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((162, 195))
                    user_turn = 1

            elif pygame.Rect(290, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 195))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((290, 195))
                    user_turn = 1

            elif pygame.Rect(418, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 195))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((418, 195))
                    user_turn = 1

            elif pygame.Rect(162, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 316))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((162, 316))
                    user_turn = 1

            elif pygame.Rect(290, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 316))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((290, 316))
                    user_turn = 1

            elif pygame.Rect(418, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 316))
                    user_turn = 2
                elif user_turn == 2:
                    joshs_positions.append((418, 316))
                    user_turn = 1

        # Draw the board
        screen.blit(board_image, (0, 0))

        # Draw all icons in the list
        for pos in arthurs_positions:
            arthurs_face.draw(pos[0], pos[1], screen)

        for pos in joshs_positions:
            joshs_face.draw(pos[0], pos[1], screen)

        # The bottom four lines draw the canvas lines of the game board
        pygame.draw.line(screen, WHITE, (160, 78), (160, 434), 3)
        pygame.draw.line(screen, WHITE, (160, 78), (535, 78), 3)
        pygame.draw.line(screen, WHITE, (160, 434), (535, 434), 3)
        pygame.draw.line(screen, WHITE, (535, 78), (535, 434), 3)

        # Update the screen with drawing.
        pygame.display.update()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()

class Board:
    pass

# To run the game, uncomment the following line:
# board_draw()
