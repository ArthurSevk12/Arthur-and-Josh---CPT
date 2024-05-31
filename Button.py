import pygame


class Button():
    # Lines 6 to 10
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    # Line 13 is a method that calls the button to appear on the screen
    def draw(self, surface):
        action = False

        # pos gets the mouse position
        pos = pygame.mouse.get_pos()

        # the bottom if statements allows the button to have the action of being 'pressed' by the user
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Line 29 allows the image to be displayed as a button
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
