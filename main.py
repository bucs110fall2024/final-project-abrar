import pygame
import sys
import random
from src.player import Player
from src.bullet import Bullet
from src.enemy import Enemy
from src.score_manager import ScoreManager
from src.sound_manager import SoundManager

class GameController:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Generic Shooter")
        self.clock = pygame.time.Clock()

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)

        # Models
        self.player = Player(self.WIDTH, self.HEIGHT)
        self.bullets = []
        self.enemies = []
        self.score_manager = ScoreManager()
        self.sound_manager = SoundManager("assets")

        # State
        self.running = True

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(None, size)
        rendered_text = font.render(text, True, color)
        self.screen.blit(rendered_text, (x, y))

    def main_menu(self):
        while True:
            self.screen.fill(self.WHITE)
            self.draw_text("GENERIC SHOOTER", 48, self.BLACK, self.WIDTH // 2 - 150, self.HEIGHT // 2 - 150)
            self.draw_text("Controls:", 36, self.BLACK, self.WIDTH // 2 - 70, self.HEIGHT // 2 - 60)
            self.draw_text("Arrow Keys or WASD to Move", 24, self.BLACK, self.WIDTH // 2 - 140, self.HEIGHT // 2 - 20)
            self.draw_text("Spacebar to Shoot", 24, self.BLACK, self.WIDTH // 2 - 90, self.HEIGHT // 2 + 10)
            self.draw_text("Press ENTER to Start", 36, self.BLACK, self.WIDTH // 2 - 120, self.HEIGHT // 2 + 80)
            self.draw_text("Press ESC to Quit", 36, self.BLACK, self.WIDTH // 2 - 120, self.HEIGHT // 2 + 120)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

    def game_over_screen(self):
        while True:
            self.screen.fill(self.WHITE)
            self.draw_text("GAME OVER", 48, self.RED, self.WIDTH // 2 - 120, self.HEIGHT // 2 - 100)
            self.draw_text(f"Time Survived: {self.score_manager.get_time_survived()}s", 36, self.BLACK, self.WIDTH // 2 - 150, self.HEIGHT // 2)
            self.draw_text(f"Kills: {self.score_manager.kills}", 36, self.BLACK, self.WIDTH // 2 - 60, self.HEIGHT // 2 + 50)
            self.draw_text("Press ENTER to Restart", 36, self.BLACK, self.WIDTH // 2 - 150, self.HEIGHT // 2 + 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

            pygame.display.flip()
            self.clock.tick(60)

    def spawn_enemy(self):
        if random.random() < 0.02:
            self.enemies.append(Enemy(self.WIDTH))

    def handle_collisions(self):
        for enemy in self.enemies[:]:
            enemy.update(self.player)
            enemy.draw(self.screen)

            for bullet in self.bullets[:]:
                if enemy.collides_with_bullet(bullet):
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score_manager.kills += 1
                    self.sound_manager.play_random_sound()
                    break

            if enemy.collides_with_player(self.player):
                self.score_manager.end_game()
                self.running = False

    def run_game(self):
        self.running = True
        self.player = Player(self.WIDTH, self.HEIGHT)
        self.bullets = []
        self.enemies = []
        self.score_manager = ScoreManager()

        while self.running:
            self.screen.fill(self.WHITE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bullets.append(Bullet(self.player.x + self.player.size // 2, self.player.y))

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            for bullet in self.bullets[:]:
                if not bullet.update():
                    self.bullets.remove(bullet)
                bullet.draw(self.screen)

            self.spawn_enemy()
            self.handle_collisions()

            self.player.draw(self.screen)
            self.draw_text(f"TIME SURVIVED: {self.score_manager.get_time_survived()}", 24, self.BLACK, 10, 10)
            self.draw_text(f"KILLS: {self.score_manager.kills}", 24, self.BLACK, self.WIDTH - 120, 10)

            pygame.display.flip()
            self.clock.tick(60)

        self.score_manager.save_score()
        self.game_over_screen()

    def run(self):
        self.main_menu()
        while True:
            self.run_game()

if __name__ == "__main__":
    game = GameController()
    game.run()