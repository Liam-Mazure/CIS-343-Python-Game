import pygame
WHITE = (255,255,255)

class Brick(pygame.sprite.Sprite):
    
    def __init__(self, color, height, weight):
        super().__init__()
    
        self.image = pygame.Surface([30, 30])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.pygame.draw.rect(self.image, (40,150,67),[0,0,30,30])

        self.rect = self.image.get_rect
