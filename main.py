import pygame

class Game:
    def __init__(self):
        self._running = True
        self._display = None
        self.size = self.weight, self.height = 640, 400
    def on_init(self):
        pygame.init()
        self._display = pygame.pygame.Overlay.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
    def on_action(self, action):
        if action.type == pygame.QUIT:
            self._running = False
    def on_loop(self):
        pass
    def on_render(self):
        pass
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init() == False:
            self._running == False
        
        while(self._running):
            for action in pygame.event.get():
                self.on_action(action)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    runGame = Game()

# class Overlay:
#     pass
# class Paddle:
#     pass
# class Ball:
#     pass
# class Brick:
#     pass