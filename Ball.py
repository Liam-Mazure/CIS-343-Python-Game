import pygame
from random import randint
from pygame import mixer

WHITE = (255,255,255)
BLACK = (0,0,0)

#This class contains logic for the game balls
class Ball(pygame.sprite.Sprite):

    #Constructor to create a new ball
    #@param self: the actual ball object
    #@param color: the color of the ball
    #@param width: the width of the ball
    #@param height: the height of the ball
    def __init__(self, color, width, height):
        super(Ball, self).__init__()

        #Creating the ball rectangle
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Drawing the rectangle
        pygame.draw.rect(self.image, color, [0,0,width,height])

        #self.velocity = [randint(4,8),randint(-8,8)]
        self.velocity = [3,3]
        self.rect = self.image.get_rect()

    #Moves the ball
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #If self hits edge of window change direction
        ball_bounce_snd = mixer.Sound('bounce_ball.wav')

        #Ball hits right wall
        if self.rect.x >= 490:
            self.velocity[0] = -self.velocity[0]
            ball_bounce_snd.play()
        
        #Ball hits left wall
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
            ball_bounce_snd.play()

        #Ball hits Top wall
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]
            ball_bounce_snd.play()

    #Function that tells the ball object to bounce off of an object
    #@param self: the actual ball object
    def bounce(self):
        ball_bounce_snd = mixer.Sound('bounce_ball.wav')
        self.velocity[0] = self.velocity[0] 
        self.velocity[1] = -self.velocity[1]
        ball_bounce_snd.play()