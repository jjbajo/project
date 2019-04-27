import pygame
#from pygame.sprite import Sprite
#from pygame import Surface
from cubes import Cube
from Player import Player
size = (640, 480)
window = pygame.display.set_mode(size)
pygame.display.set_caption('The Game')
screen = pygame.Surface((size))



#class Cube(Sprite):
#    def __init__(self, x, y):
#        Sprite.__init__(self)
#        self.image = load('box.png')
#        self.rect = self.image.get_rect()
#        self.rect.x = x
#        self.rect.y = y

hero = Player(100, 55)
left = right = up = down = False


level = ['----------------',
         '-              -',
         '-   ---        -',
         '-              -',
         '-             --',
         '-              -',
         '-  ---         -',
         '-         ---  -',
         '-      -       -',
         '-      -       -',
         '-              -',
         '----------------',
         ]

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)

boxes = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            bx = Cube(x, y)
            sprite_group.add(bx)
            boxes.append(bx)
        x = x + 40
    y = y + 40
    x = 0

#bx = pygame.Surface((40, 40))
#bx = pygame.image.load('box.png')


wheel = True
clock = pygame.time.Clock()

while wheel:
    clock.tick(25)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            wheel = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                left = True
            if e.key == pygame.K_d:
                right = True
            if e.key == pygame.K_s:
                down = True
            if e.key == pygame.K_w:
                up = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_a:
                left = False
            if e.key == pygame.K_d:
                right = False
            if e.key == pygame.K_s:
                down = False
            if e.key == pygame.K_w:
                up = False


    screen.fill((10, 120, 10))
    #level_maker(level, bx)

    hero.update(left, right, up, down, boxes)

    #hero.draw(screen)
    sprite_group.draw(screen)
    window.blit(screen, (0, 0))

    pygame.display.flip()













