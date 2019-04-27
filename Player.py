from pygame.sprite import Sprite, collide_rect
from pygame import Surface


speed = 3


class Player(Sprite):
    def __init__(self, x, y ):
        # чтобы связать класс игрок с классом спрайт
        Sprite.__init__(self)
        self.image = Surface((22, 22))
        self.image.fill((150, 150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




    def update(self, left, right, up, down, boxes):
         if left:
                self.rect.x -= speed
         if right:
                self.rect.x += speed
         if up:
                self.rect.y -= speed
         if down:
                self.rect.y += speed


         self.collide(right, left, up, down, boxes)


#    def draw(self, surf):
#        surf.blit(self.image, (self.rect.x, self.rect.y))

    def collide(self, right, left, up, down, boxes):
        for bx in boxes:
            if self.rect.colliderect(bx.rect):
                if right:
                    self.rect.right = bx.rect.left
                if left:
                    self.rect.left = bx.rect.right
                if down:
                    self.rect.bottom = bx.rect.top
                if up:
                    self.rect.top = bx.rect.bottom






