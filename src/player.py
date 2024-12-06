import pygame

GREEN = (0, 255, 0)

class Player:
    def __init__(self, screen_width, screen_height):
        self.size = 30
        self.x = screen_width // 2 - self.size // 2
        self.y = screen_height - 60
        self.speed = 3
        self.color = (0, 255, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def move(self, keys):
        # Arrow keys
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Left arrow or A
            self.x -= self.speed if self.x > 0 else 0
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Right arrow or D
            self.x += self.speed if self.x < 800 - self.size else 0
        if keys[pygame.K_UP] or keys[pygame.K_w]:  # Up arrow or W
            self.y -= self.speed if self.y > 0 else 0
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Down arrow or S
            self.y += self.speed if self.y < 600 - self.size else 0
