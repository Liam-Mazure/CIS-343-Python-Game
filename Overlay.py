import pygame
WHITE = (255,255,255)


class Overlay:

    __score = 0
    __lives = 0

    def __init__(self,lives):
        self.__lives = lives

    def get_lives(self):
        return self.__lives
    
    def set_lives(self, num):
        self.__lives = num

    def get_score(self):
        return self.__score
    
    def set_score(self, num):
        self.__score = num
    
    def Draw(self,window):
        font = pygame.font.Font(None, 20)
        text = font.render("Score: " + str(Overlay.get_score(self)),1,WHITE)
        window.blit(text, (5,10))
        text = font.render("Lives: " + str(Overlay.get_lives(self)),1,WHITE)
        window.blit(text, (5,30))
        

   # def sub_life(self):
    #    self.set_lives(self.get_lives() - 1)
        




