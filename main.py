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

    block = Brick(BLUE,50,30)
    paddle = Paddle(125, 20, 1)
    ball = Ball(BLACK, 25, 25)

    paddle.rect.x = 250
    paddle.rect.y = 450
    
    ball.rect.x = 250
    ball.rect.y = 250

    all_blocks = pygame.sprite.pygame.sprite.Group()
    for i in range(10):
        block = Brick(BLUE,50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 0
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick(BLACK,50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 30
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick(BLACK,50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 60
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick(BLACK,50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 90
        our_sprites.add(block)
        all_blocks.add(block)
    for i in range(10):
        block = Brick(BLUE,50,30)
        block.rect.x = 0 + i * 50
        block.rect.y = 120
        our_sprites.add(block)
        all_blocks.add(block)

    our_sprites.add(block)
    our_sprites.add(paddle)
    our_sprites.add(ball)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        
    
        #Moves paddel left and right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            paddle.moveRight(5)

        # Game Logic
        our_sprites.update()

        #If ball hits edge of window change direction
        if ball.rect.x >= 475:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y >= 475:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y <= 0:
            ball.velocity[1] = -ball.velocity[1]

        #If ball hits paddle bounce off
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x -= ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()

        
        block_list = pygame.sprite.spritecollide(ball,all_blocks,False)
        for block in block_list:
            block.hit()
            ball.bounce()

        # Drawing Logic
        window.fill(WHITE)

        our_sprites.draw(window)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()