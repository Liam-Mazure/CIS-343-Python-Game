import pygame
from pygame import mixer
WHITE = (255,255,255)

#This class is the logic for all the bricks
#In the brick breaker game
class Brick(pygame.sprite.Sprite):

<<<<<<< Updated upstream
    #Private variable, health of the brick
    __Health = 0
    
    #Constructor for the Brick
    #@param self: the object itself
    #@param color: the color of the brick
    #@param width: the width of the brick
    #@param height: the height of the brick
=======
    #Initializes private varibale Health
    __Health = 0
    
    #Sets health of block to its RGB values subtracted from 766(max color value)
>>>>>>> Stashed changes
    def __init__(self, color, width, height):
        x = color[0]
        y = color[1]
        z = color[2]

        #Set the health of the brick to 766 - the RGB values of the brick
        self.setHealth(766-x-y-z)
        super(Brick, self).__init__()

        #Creating the actual rectangle brick
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Draws block
        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.rect = self.image.get_rect()
    
<<<<<<< Updated upstream
    #Function to return the health of the brick
    #@param self: The actual brick object
    def getHealth(self):
        return self.__Health
    
    #Function to set/update the health of a brick object
    #@param self: the actual brick object
    #@param value: the value that health should be set to
    def setHealth(self,value):
        self.__Health = value
    
    #Function to register that a block has been hit
    #Takes away health and kills the brick if health is 
    #zero or less
    #@param self: the actual brick object
=======
    #Returns current health
    def getHealth(self):
        return self.__Health
    
    #Sets health to value
    def setHealth(self,value):
        self.__Health = value
    
    #When block is hit subtract 25 from health and check if blocks health is less than or equal to 0. If so destroy block with sound
>>>>>>> Stashed changes
    def hit(self):
        break_block_snd = mixer.Sound('explosion.wav')

        #Take away 25 health from the brick
        self.setHealth(self.getHealth() - 25)
        
        #If health is 0 or less kill the brick and play break sound
        if self.getHealth() <= 0:
            self.kill()
            break_block_snd.play()