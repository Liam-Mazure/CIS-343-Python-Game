import pygame
WHITE = (255,255,255)

class Brick(pygame.sprite.Sprite):

    __Health = 0
    
    def __init__(self, color, width, height):
        x = color[0]
        y = color[1]
        z = color[2]
        self.setHealth(766-x-y-z)
        super(Brick, self).__init__()
    
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0,0,width,height])

        self.rect = self.image.get_rect()
    
    def getHealth(self):
        return self.__Health
    
    def setHealth(self,value):
        self.__Health = value
    
    def hit(self):
        self.setHealth(self.getHealth() - 25)
        if self.getHealth() <= 0:
            self.kill()