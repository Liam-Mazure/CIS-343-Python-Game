import pygame

WHITE = (255,255,255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Ball, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.circle(self.image, color, (250,250),25)

        self.rect = self.image.get_rect()