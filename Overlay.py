import pygame
WHITE = (255,255,255)


class Overlay:

    #Initializes private variables score and lives
    __score = 0
    __lives = 0

    def __init__(self,lives):
        self.__lives = lives

    #Returns current lives
    def get_lives(self):
        return self.__lives
    
    #Sets lives to num
    def set_lives(self, num):
        self.__lives = num

    #Returns current score
    def get_score(self):
        return self.__score
    
    #Sets score to num
    def set_score(self, num):
        self.__score = num
    
    #Draws current score and lives to top left of screen
    def Draw(self,window):
        font = pygame.font.Font(None, 20)
        text = font.render("Score: " + str(Overlay.get_score(self)),1,WHITE)
        window.blit(text, (5,10))
        text = font.render("Lives: " + str(Overlay.get_lives(self)),1,WHITE)
        window.blit(text, (5,30))

<<<<<<< Updated upstream
        

=======
>>>>>>> Stashed changes



