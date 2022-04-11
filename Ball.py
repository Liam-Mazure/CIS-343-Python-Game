import pygame
from random import randint
from pygame import mixer

WHITE = (255,255,255)
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Ball, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Draws Ball
        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.velocity = [3,3]
        self.rect = self.image.get_rect()

    #Keeps balls veelocity constent if there is no change inflicted on the ball
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #If self hits edge of window change direction
        ball_bounce_snd = mixer.Sound('bounce_ball.wav')
        if self.rect.x >= 490:
            self.velocity[0] = -self.velocity[0]
            ball_bounce_snd.play()
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
            ball_bounce_snd.play()
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]
            ball_bounce_snd.play()

    #Flips balls velocity of vertical movement, but keeps velocity of horizonatl movement the same if ball bounces
    def bounce(self):
        ball_bounce_snd = mixer.Sound('bounce_ball.wav')
        self.velocity[0] = self.velocity[0] 
        self.velocity[1] = -self.velocity[1]
        ball_bounce_snd.play()