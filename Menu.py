import pygame
from Button import Button
from GameBoard import Board, board_draw
from How_To_Play_Menu import draw_how_2_play_menu

size = (700, 500)
screen = pygame.display.set_mode(size)

board = Board


class Menu():
    # pygame.display.set_caption('Tic Tac Toe')
    menu_img = pygame.image.load('Menu.png').convert_alpha()
    start_img = pygame.image.load('START_button.png').convert_alpha()
    how_2_play_img = pygame.image.load('HOW_TO_PLAY_button.png').convert_alpha()
    how_2_play_menu = pygame.image.load('How_To_Play_Menu.png').convert_alpha()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SAND = (225, 198, 153)

    start_button = Button(300, 310, start_img)
    how_2_play_button = Button(300, 370, how_2_play_img)

    done = False


    clock = pygame.time.Clock()

    while not done:
        screen.blit(menu_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if start_button.draw(screen):
            done = True
            board_draw()

        if how_2_play_button.draw(screen):
            done = True
            draw_how_2_play_menu()

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()