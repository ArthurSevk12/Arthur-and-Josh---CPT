import pygame


def board_draw():
    # Define some colors
    WHITE = (255, 255, 255)

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
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                done = True
            #print(pos)

            if pygame.Rect(162, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change')
            elif pygame.Rect(290, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x2')
            elif pygame.Rect(418, 83, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x3')
            elif pygame.Rect(162, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x4')
            elif pygame.Rect(290, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x5')
            elif pygame.Rect(418, 195, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x6')
            elif pygame.Rect(162, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x7')
            elif pygame.Rect(290, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x8')
            elif pygame.Rect(418, 316, 115, 112).collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                print('Click to change x9')

        screen.blit(board_image, (0, 0))

        # The bottom four lines draw the canvas lines of the game board
        pygame.draw.line(screen, WHITE, (160, 78), (160, 434), 3)
        pygame.draw.line(screen, WHITE, (160, 78), (535, 78), 3)
        pygame.draw.line(screen, WHITE, (160, 434), (535, 434), 3)
        pygame.draw.line(screen, WHITE, (535, 78), (535, 434), 3)



        # Update the screen with drawing.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


class Board:
    pass
