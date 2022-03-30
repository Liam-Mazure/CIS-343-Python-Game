import pygame
WHITE = (255,255,255)

class Brick(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super(Brick, self).__init__()
    
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.rect = self.image.get_rect()
