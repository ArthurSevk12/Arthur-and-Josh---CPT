import pygame
from Icon import Icon


def board_draw():
    # Define some colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    board_image = pygame.image.load('Gameboard.png').convert_alpha()
    arthurs_img = pygame.image.load('Arthurs_Face_CPT.png').convert_alpha()
    joshs_img = pygame.image.load('Joshuas_Face_CPT.png').convert_alpha()
    user_1_img = pygame.image.load('User_1_Winner.png').convert_alpha()
    user_2_img = pygame.image.load('User_2_Winner.png').convert_alpha()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Tic-Tac-Toe!")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    arthurs_face = Icon(arthurs_img)
    joshs_face = Icon(joshs_img)
    user_1_won = Icon(user_1_img)
    user_2_won = Icon(user_2_img)

    # List to store positions of icons
    arthurs_positions = []
    joshs_positions = []

    # the bottom square variables are the squares of the Tic Tac Toe board canvas.
    square1 = 0
    square2 = 0
    square3 = 0
    square4 = 0
    square5 = 0
    square6 = 0
    square7 = 0
    square8 = 0
    square9 = 0
    user_turn = 1

    # the bottom function gets the squares and outputs the winning user
    def count_squares(first_square, second_square, third_square):
        if first_square == 1 and second_square == 1 and third_square == 1:
            screen.fill(BLACK)
            user_1_won.draw(0, 0, screen)
        elif first_square == 2 and second_square == 2 and third_square == 2:
            screen.fill(BLACK)
            user_2_won.draw(0, 0, screen)

    while not done:
        # --- Main event loop

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True

            # The bottom if statements get the mouse position and determines which square on the Tik Tac Toe board the
            # user has clicked
            if pygame.Rect(162, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 83))
                    user_turn = 2
                    square1 = 1
                elif user_turn == 2:
                    joshs_positions.append((162, 83))
                    user_turn = 1
                    square1 = 2

            elif pygame.Rect(290, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 83))
                    user_turn = 2
                    square2 = 1
                elif user_turn == 2:
                    joshs_positions.append((290, 83))
                    user_turn = 1
                    square2 = 2

            elif pygame.Rect(418, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 83))
                    user_turn = 2
                    square3 = 1
                elif user_turn == 2:
                    joshs_positions.append((418, 83))
                    user_turn = 1
                    square3 = 2

            elif pygame.Rect(162, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 195))
                    user_turn = 2
                    square4 = 1
                elif user_turn == 2:
                    joshs_positions.append((162, 195))
                    user_turn = 1
                    square4 = 2

            elif pygame.Rect(290, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 195))
                    user_turn = 2
                    square5 = 1
                elif user_turn == 2:
                    joshs_positions.append((290, 195))
                    user_turn = 1
                    square5 = 2

            elif pygame.Rect(418, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 195))
                    user_turn = 2
                    square6 = 1
                elif user_turn == 2:
                    joshs_positions.append((418, 195))
                    user_turn = 1
                    square6 = 2

            elif pygame.Rect(162, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((162, 316))
                    user_turn = 2
                    square7 = 1
                elif user_turn == 2:
                    joshs_positions.append((162, 316))
                    user_turn = 1
                    square7 = 2

            elif pygame.Rect(290, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((290, 316))
                    user_turn = 2
                    square8 = 1
                elif user_turn == 2:
                    joshs_positions.append((290, 316))
                    user_turn = 1
                    square8 = 2

            elif pygame.Rect(418, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if user_turn == 1:
                    arthurs_positions.append((418, 316))
                    user_turn = 2
                    square9 = 1
                elif user_turn == 2:
                    joshs_positions.append((418, 316))
                    user_turn = 1
                    square9 = 2

        # Draw the board
        screen.blit(board_image, (0, 0))

        # Lines 154 to 158 Draws all icons in the list onto the screen
        for pos in arthurs_positions:
            arthurs_face.draw(pos[0], pos[1], screen)

        for pos in joshs_positions:
            joshs_face.draw(pos[0], pos[1], screen)

        # The bottom four lines
        pygame.draw.line(screen, WHITE, (160, 78), (160, 434), 3)
        pygame.draw.line(screen, WHITE, (160, 78), (535, 78), 3)
        pygame.draw.line(screen, WHITE, (160, 434), (535, 434), 3)
        pygame.draw.line(screen, WHITE, (535, 78), (535, 434), 3)

        # Calling the count_squares function wil determine which user won
        count_squares(square1, square2, square3)
        count_squares(square4, square5, square6)
        count_squares(square7, square8, square9)
        count_squares(square1, square4, square7)
        count_squares(square2, square5, square8)
        count_squares(square3, square6, square9)
        count_squares(square1, square5, square9)
        count_squares(square3, square5, square7)

        # The bottom four lines draw the canvas lines of the game board

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
