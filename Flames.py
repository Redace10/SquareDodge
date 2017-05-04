import random
import threading
import time
import pygame

# class for the five fire balls
class Flames(threading.Thread):
    def __init__(self, gameDisplay):
        threading.Thread.__init__(self)
        self.thread = threading.Thread(target=self.run)
        self.gameDisplay = gameDisplay

        self.level = 0
        self.fire_speed = 1
        self.fire_rect = pygame.rect.Rect((1270, random.randint(30, 570), 20, 20))
        self.run_flame = True

    def run(self):
        while self.run_flame:
            if self.fire_rect.x <= 10:
                self.fire_rect = pygame.rect.Rect((1270, random.randint(30, 570), 20, 20))
                self.level += 1

            self.fire_rect.move_ip(-self.fire_speed, 0)
            time.sleep(0.001)
            pygame.draw.rect(self.gameDisplay, (255, 0, 0), self.fire_rect)
            pygame.display.update(self.fire_rect)
