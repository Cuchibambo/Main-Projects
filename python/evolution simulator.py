import pygame

class main:
    def __init__(self,screen_resolution) -> None:
        self.screen_resolution = self.screen_resolution
        self.screen = pygame.display.set_mode(self.screen_resolution)
    def run(self):
        pygame.init()
        