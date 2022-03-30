import pygame
from Brick import Brick
from Paddle import Paddle
from Ball import Ball
WHITE = (255, 255, 255)
BLUE = (26,78,125)
BLACK = (0,0,0)


class Game:
    pygame.init()
    size = (500,500)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")

    carryOn = True
    
    clock = pygame.time.Clock()

    our_sprites = pygame.sprite.Group()

    block = Brick(BLUE,100,30)
    paddle = Paddle(125, 20, 1)
    ball = Ball(BLACK, 25, 25)

    paddle.rect.x = 250
    paddle.rect.y = 450
    
    ball.rect.x = 250
    ball.rect.y = 250

    our_sprites.add(block)
    our_sprites.add(paddle)
    our_sprites.add(ball)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        
    
    
        # Game Logic
        our_sprites.update()

        # Drawing Logic
        window.fill(WHITE)

        our_sprites.draw(window)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()