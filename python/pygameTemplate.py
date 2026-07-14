import pygame

# Colors
background_color = "#333333"

class main:
    def __init__(self):
        self.running = True
        # Time and delta time
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.dt = 1/self.FPS
    def run(self):
        # Start Pygame
        pygame.init()
        self.font = pygame.font.SysFont('Monospace', 22, bold=False)
        self.width, self.height = 500, 500
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.screen.fill(background_color)
        pygame.display.flip()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case 1:
                            self.leftClick(pygame.mouse.get_pos())
                        case 3:
                            self.rightClick(pygame.mouse.get_pos())
            self.clock.tick(self.FPS) # appply fps
            self.update()
            pygame.display.flip() # Update Screen

    def update(self):
        self.screen.fill(background_color)
    
    def leftClick(self,MousePos):
        return
    
    def rightClick(self,MousePos):
        return
