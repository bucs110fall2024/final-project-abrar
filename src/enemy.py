import pygame
import random
import math

RED = (255, 0, 0)

class Enemy:
    def __init__(self, width):
        self.size = 30
        self.x = random.randint(0, width - self.size)
        self.y = random.randint(-100, -self.size)  # Start above the screen
        self.speed = random.uniform(1.5, 3.5)  # Randomized speed

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))

    def update(self, player):
        """Move towards the player's position."""
        dx = player.x - self.x
        dy = player.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance > 0:  # Avoid division by zero
            self.x += self.speed * (dx / distance)
            self.y += self.speed * (dy / distance)

        return True  # Always stays on screen for chasing

    def collides_with_bullet(self, bullet):
        return (
            self.x < bullet.x < self.x + self.size
            and self.y < bullet.y < self.y + self.size
        )

    def collides_with_player(self, player):
        return (
            self.x < player.x + player.size
            and self.x + self.size > player.x
            and self.y < player.y + player.size
            and self.y + self.size > player.y
        )