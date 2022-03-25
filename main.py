import pygame
import Brick
WHITE = (255, 255, 255)


class Game:
    pygame.init()
    size = (500,500)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Brick Breaker")

    carryOn = True
    
    clock = pygame.time.Clock()

    our_sprites = pygame.sprite.Group()

    block = Brick((26,78,125),30,30)

    our_sprites.add(block)

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
        
    
    
        # Game Logic


        # Drawing Logic
        window.fill(WHITE)

        our_sprites.draw(window)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

    # def __init__(self):
    #     self._running = True
    #     self._display = None
    # def on_init(self):
    #     pygame.init()
    #     self._display = pygame.pygame.Overlay.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    #     self._running = True
    # def on_action(self, action):
    #     if action.type == pygame.QUIT:
    #         self._running = False
    # def on_loop(self):
    #     pass
    # def on_render(self):
    #     pass
    # def on_cleanup(self):
    #     pygame.quit()
    # def on_execute(self):
    #     if self.on_init() == False:
    #         self._running == False
        
    #     while(self._running):
    #         for action in pygame.event.get():
    #             self.on_action(action)
    #         self.on_loop()
    #         self.on_render()
    #     self.on_cleanup()

# if __name__ == "__main__":
#     runGame = Game()

# class Overlay:
#     pass
# class Paddle:
#     pass
# class Ball:
#     pass
# class Brick(pygame.sprite.Sprite):
    
#     def __init__(self, color, height, weight):
#         super().__init__()
    
#         self.image = pygame.Surface([30, 30])
#         self.image.fill(WHITE)
#         self.image.set_colorkey(WHITE)

#         pygame.draw.pygame.draw.rect(self.image, (40,150,67),[0,0,30,30])

#         self.rect = self.image.get_rect
