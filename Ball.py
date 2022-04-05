import pygame
from random import randint

WHITE = (255,255,255)

class self(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(self, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0,0,width,height])

        #self.velocity = [randint(4,8),randint(-8,8)]
        self.velocity = [3,3]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        #experimental 
        #If self hits edge of window change direction
        if self.rect.x >= 490:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        if self.rect.y >= 490:
            overlay.set_lives(overlay.get_lives()-1)
            self.rect.x = 250
            self.rect.y = 250
            pygame.time.wait(1000)
            if(overlay.get_lives() == -1):
                font = pygame.font.Font(None, 74)
                text = font.render("Game Over", 1, BLACK)
                window.blit(text, (120, 250))
                pygame.display.flip()
                pygame.time.wait(3000)
                carryOn = False
        if self.rect.y <= 0:
            self.velocity[1] = -self.velocity[1]

        #If self hits paddle bounce off
        if pygame.sprite.collide_mask(self, paddle):
            self.rect.x -= self.velocity[0]
            self.rect.y -= self.velocity[1]
            self.bounce()

        #self hits Block
        block_list = pygame.sprite.spritecollide(self,all_blocks,False)
        for block in block_list:
            block.hit()
            self.bounce()
            if block.getHealth() <= 0:
                overlay.set_score(overlay.get_score() + 1)

    def bounce(self):
        self.velocity[0] = self.velocity[0] 
        self.velocity[1] = -self.velocity[1]