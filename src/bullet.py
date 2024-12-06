import pygame

YELLOW = (255, 255, 0)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 5
        self.speed = 7

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.size)

    def update(self):
        self.y -= self.speed
        return self.y > 0
