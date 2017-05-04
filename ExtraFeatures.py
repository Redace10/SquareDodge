import pygame

class Features():

    def __init__(self, gameDisplay):
        self.gameDisplay = gameDisplay

    def message_to_screen(self, msg, color, size):
        font = pygame.font.SysFont(None, size)
        screen_text = font.render(msg, True, color)
        return screen_text