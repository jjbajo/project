from pygame.sprite import Sprite
from pygame.image import load


class Cube(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = load('box.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y