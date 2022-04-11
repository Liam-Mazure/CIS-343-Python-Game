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

        #Draws paddle
        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])

        self.rect = self.image.get_rect()

    #Moves paddle left
    def moveLeft(self,pixels):
        self.rect.x -= pixels

        #Prevents paddle from leaving window on left side
        if self.rect.x < 0:
            self.rect.x = 0

    #Moves paddle right 
    def moveRight(self,pixels):
        self.rect.x += pixels

        #Prevents paddle from leaving window on right side
        if self.rect.x > 375:
            self.rect.x = 375

    #Pairs moveRght() and moveLeft() functions to keys and number of pixles to move with each press
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            self.moveRight(5)