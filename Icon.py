import pygame


class Icon:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def draw(self, x, y, surface):
        self.rect.topleft = (x, y)
        surface.blit(self.image, (self.rect.x, self.rect.y))
