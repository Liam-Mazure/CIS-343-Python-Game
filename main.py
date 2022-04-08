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


class Game:
    pygame.init()
    size = (500,500)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")
    mixer.music.load('background.wav')
    mixer.music.play(-1)


    carryOn = True
    
    clock = pygame.time.Clock()

    our_sprites = pygame.sprite.Group()

    ball_list = pygame.sprite.pygame.sprite.Group()
    ball = Ball(BLACK, 10, 10)
    ball_list.add(ball)

    paddle = Paddle(125, 20, 1)
    overlay = Overlay(3)

    paddle.rect.x = 250
    paddle.rect.y = 450
    
    ball.rect.x = 250
    ball.rect.y = 250

    #Adds rows of blocks
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

    #Main Game Loop
    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
    
        #Add Extra ball
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            ball = Ball(BLACK,10,10)
            ball.rect.x = 250
            ball.rect.y = 250
            our_sprites.add(ball)
            ball_list.add(ball)

        # Game Logic
        our_sprites.update()

        #Checks if ball passes paddle
        for ball in ball_list:
            if ball.rect.y >= 490:
                if len(ball_list) == 1:
                    overlay.set_lives(overlay.get_lives()-1)
                ball.rect.x = 250
                ball.rect.y = 250
                if len(ball_list) == 1:
                    pygame.time.wait(1000)
                else:
                    ball.kill()
                if(overlay.get_lives() == -1):
                    font = pygame.font.Font(None, 74)
                    text = font.render("Game Over", 1, BLACK)
                    window.blit(text, (120, 250))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    carryOn = False

        #If ball hits paddle bounce off
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
                if block.getHealth() <= 0:
                    overlay.set_score(overlay.get_score() + 1)
        
        # Drawing Logic
        window.fill(WHITE)

        our_sprites.draw(window)

        #Draws score and Lives
        overlay.Draw(window)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()