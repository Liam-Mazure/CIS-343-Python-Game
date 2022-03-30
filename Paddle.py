from turtle import width
import pygame
WHITE = (255,255,255)
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, speed):
        super(Paddle, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])

        self.rect = self.image.get_rect()

    def moveLeft(self,pixels):
        self.rect.x -= pixels

        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self,pixels):
        self.rect.x += pixels

        if self.rect.x > 375:
            self.rect.x = 375