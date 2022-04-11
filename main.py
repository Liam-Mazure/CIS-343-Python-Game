from random import randint
import pygame
from Brick import Brick
from Paddle import Paddle
from Ball import Ball
from Overlay import Overlay
from pygame import mixer 
WHITE = (255, 255, 255)
BLUE = (26,78,125)
BLACK = (0,0,0)

#This class is the main game
class Game:
    pygame.init()

    #Game Size
    size = (500,500)
    window = pygame.display.set_mode(size)

    #Title of window
    pygame.display.set_caption("Brick Breaker")

    #Background Music
    mixer.music.load('background.wav')
    mixer.music.play(-1)

    #Keep the game running
    carryOn = True
    
    #Clock for timing aspects of the game
    clock = pygame.time.Clock()

    #List of all the sprites we have in our game
    our_sprites = pygame.sprite.Group()

    #List of all the balls we have in the game
    ball_list = pygame.sprite.pygame.sprite.Group()

    #Creating our first ball object and adding it to the ball list
    ball = Ball(BLACK, 10, 10)
    ball_list.add(ball)

    #Creating the overlay and Paddle used in the game
    paddle = Paddle(125, 20, 1)
    overlay = Overlay(3)

    #Putting the ball and paddle in the correct starting positions
    paddle.rect.x = 250
    paddle.rect.y = 450
    ball.rect.x = 250
    ball.rect.y = 250

<<<<<<< Updated upstream
    #Adds rows of blocks to the screen
=======
    #Adds 5 Rows of 10 blocks each with a random color
>>>>>>> Stashed changes
    all_blocks = pygame.sprite.pygame.sprite.Group()
    for i in range(10):
        block = Brick((randint(0,255),randint(0,255),randint(0,255)),50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 0
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick((randint(0,255),randint(0,255),randint(0,255)),50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 30
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick((randint(0,255),randint(0,255),randint(0,255)),50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 60
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick((randint(0,255),randint(0,255),randint(0,255)),50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 90
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick((randint(0,255),randint(0,255),randint(0,255)),50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 120
        our_sprites.add(block)
        all_blocks.add(block)

    #Adding Initial Sprites to our sprite list
    our_sprites.add(block)
    our_sprites.add(paddle)
    our_sprites.add(ball)
<<<<<<< Updated upstream

    #Main Game Loop
=======
    
>>>>>>> Stashed changes
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
    
        #Add Extra ball
<<<<<<< Updated upstream
        keys = pygame.key.get_pressed()
        
        #'B' Key pressed add a ball
        if keys[pygame.K_b]:
            
            #Create a new ball and put it in the middle
            #Of the screen and add it to the sprite groups
            ball = Ball(BLACK,10,10)
            ball.rect.x = 250
            ball.rect.y = 250
            our_sprites.add(ball)
            ball_list.add(ball)

        # Game Logic

        #Update all our sprites in the sprite group
=======
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_b:
                    ball = Ball(BLACK,10,10)
                    ball.rect.x = 250
                    ball.rect.y = 250
                    our_sprites.add(ball)
                    ball_list.add(ball)
       # keys = pygame.key.get_pressed()
        #if keys[pygame.K_b]:
        #    ball = Ball(BLACK,10,10)
         #   ball.rect.x = 250
          #  ball.rect.y = 250
           # our_sprites.add(ball)
            #ball_list.add(ball)

        #Updates all sprites
>>>>>>> Stashed changes
        our_sprites.update()

        #Checks if ball passes paddle now that everything
        #is updated for every ball on the screen
        for ball in ball_list:
            
            #Ball is below the paddle, check if life should be taken away
            if ball.rect.y >= 490:
                
                #Check number of balls on the screen
                #If only 1 take away a life and put the ball
                #to the middle of the screen
                if len(ball_list) == 1:
                    overlay.set_lives(overlay.get_lives()-1)
                ball.rect.x = 250
                ball.rect.y = 250
                if len(ball_list) == 1:
                    pygame.time.wait(1000)
                
                #There is more than 1 ball on the screen
                #Just delete the ball and don't take away a life
                else:
                    ball.kill()
                
                #Check if player is out of lives and end game
                #if they are
                if(overlay.get_lives() == -1):
                    font = pygame.font.Font(None, 74)
                    text = font.render("Game Over", 1, BLACK)
                    window.blit(text, (120, 250))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    carryOn = False

        #If any ball hits the paddle: bounce off
        for ball in ball_list:
            if pygame.sprite.collide_mask(ball, paddle):
                ball.rect.x -= ball.velocity[0]
                ball.rect.y -= ball.velocity[1]
                ball.bounce()

            #Ball hits Block
            block_list = pygame.sprite.spritecollide(ball,all_blocks,False)
            for block in block_list:
                block.hit()
                ball.bounce()

                #If block is destroyed add 1 to score
                if block.getHealth() <= 0:
                    overlay.set_score(overlay.get_score() + 1)
        
<<<<<<< Updated upstream
        # Drawing Logic
        window.fill(WHITE)

        #Draw the sprites to the window
=======
        #Fills window with color
        window.fill(WHITE)

        #Adds sprits to winow
>>>>>>> Stashed changes
        our_sprites.draw(window)

        #Draws score and Lives
        overlay.Draw(window)

        pygame.display.flip()

        clock.tick(60)

    #Exit the game
    pygame.quit()