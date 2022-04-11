import pygame
WHITE = (255,255,255)

#This class is used to keep track of the lives and score
#And also draws them to the screen
class Overlay:

    #Number of lives left and the current score
    __score = 0
    __lives = 0

    #Constructor starts the player off with lives number of lives
    #@param self: the actual overlay
    #@param lives: the number of lives a player gets to start
    def __init__(self,lives):
        self.__lives = lives

    #Used to get the number of lives the player has left
    #@param self: the actual overlay object
    #@return the number of lives the player has
    def get_lives(self):
        return self.__lives
    
    #Sets the number of lives the player has
    #@param self: the actual overlay object
    #@param num: the value to set the lives to
    def set_lives(self, num):
        self.__lives = num

    #Used to get the score that the player has
    #@param self: the actual overlay object
    #@return the score that the player has
    def get_score(self):
        return self.__score
    
    #Sets the score of the player
    #@param self: the actual overlay object
    #@param num: the value to set the score to
    def set_score(self, num):
        self.__score = num
    
    #Draws the overlay to the screen
    #@param self: the actual overlay object
    #@param window: the window to draw the screen to
    def Draw(self,window):
        font = pygame.font.Font(None, 20)
        text = font.render("Score: " + str(Overlay.get_score(self)),1,WHITE)
        window.blit(text, (5,10))
        text = font.render("Lives: " + str(Overlay.get_lives(self)),1,WHITE)
        window.blit(text, (5,30))

        




