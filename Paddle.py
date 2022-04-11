from turtle import width
import pygame
WHITE = (255,255,255)
BLACK = (0,0,0)

#This class contains all the logic for the paddle used in the game
class Paddle(pygame.sprite.Sprite):

    #Constructor used to create the paddle object
    #@param self: the actual Paddle object
    #@param width: the width of the paddle
    #@param height: the height of the paddle
    #@param speed: the speed that the paddle should move
    def __init__(self, width, height, speed):
        super(Paddle, self).__init__()

        #Drawing of the paddle object
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])

        self.rect = self.image.get_rect()

    #Function to move the paddle left
    #@param self: the acutal paddle object
    #@param pixels: the number of pixels to move the paddle
    def moveLeft(self,pixels):
        self.rect.x -= pixels

        #Make sure they can't move the paddle off the screen
        if self.rect.x < 0:
            self.rect.x = 0

    #Function to move the paddle right
    #@param self: the acutal paddle object
    #@param pixels: the number of pixels to move the paddle
    def moveRight(self,pixels):
        self.rect.x += pixels

        #Make sure they can't move the paddle off the screen
        if self.rect.x > 375:
            self.rect.x = 375

    #Checks which key was pressed and calls the appropriate function 
    #to move the paddle left or right
    #@param self: the acutal paddle object
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            self.moveRight(5)