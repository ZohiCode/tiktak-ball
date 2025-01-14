import pygame
import sys

# Pygame'i başlatma
pygame.init()


# Ayarlar sınıfı
class Settings:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BALL_SIZE = 45
    PADDLE_WIDTH = 120
    PADDLE_HEIGHT = 20
    BALL_SPEED_X = 4
    BALL_SPEED_Y = -4
    FPS = 60
    COLORS = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "blue": (0, 0, 255),
    }
    ball_img = pygame.image.load("ball.png")


# Skor fontu
FONT = pygame.font.SysFont("Arial", 24)

# Ekranı başlatma
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
pygame.display.set_caption("Tik Tak Ball - Skor Sistemi")

# FPS kontrolcüsü
clock = pygame.time.Clock()


# Oyun sınıfı
class TikTakBallGame:
    def __init__(self):
        self.settings = Settings()
        self.ball = pygame.Rect(
            375, 300, self.settings.BALL_SIZE, self.settings.BALL_SIZE
        )

        self.paddle = pygame.Rect(
            375, 550, self.settings.PADDLE_WIDTH, self.settings.PADDLE_HEIGHT
        )
        self.ball_speed = [self.settings.BALL_SPEED_X, self.settings.BALL_SPEED_Y]
        self.score = 0

        self.ball_image = pygame.image.load("ball.png")
        self.ball_image = pygame.transform.scale(
            self.ball_image, (self.settings.BALL_SIZE, self.settings.BALL_SIZE)
        )

    def reset_ball(self):
        """Topu başlangıç konumuna döndür."""
        self.ball.x, self.ball.y = (
            self.settings.SCREEN_WIDTH // 2,
            self.settings.SCREEN_HEIGHT // 2,
        )
        self.ball_speed = [self.settings.BALL_SPEED_X, -abs(self.settings.BALL_SPEED_Y)]

    def handle_collisions(self):
        """Topun çarpma mantığını kontrol et."""
        # Ekran kenarlarına çarpma
        if self.ball.left <= 0 or self.ball.right >= self.settings.SCREEN_WIDTH:
            self.ball_speed[0] = -self.ball_speed[0]
        if self.ball.top <= 0:
            self.ball_speed[1] = -self.ball_speed[1]

        # Paddle ile çarpışma
        if self.ball.colliderect(self.paddle):
            self.ball_speed[1] = -self.ball_speed[1]
            self.score += 1
            self.increase_speed()

        # Top yere düşerse
        if self.ball.bottom >= self.settings.SCREEN_HEIGHT:
            self.game_over()

    def increase_speed(self):
        """Topun hızını artırır."""
        self.ball_speed[0] *= 1.05
        self.ball_speed[1] *= 1.05

    def handle_paddle_movement(self):
        """Paddle'ın hareketini kontrol eder."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.left > 0:
            self.paddle.x -= self.settings.SCREEN_WIDTH // 100
        if keys[pygame.K_RIGHT] and self.paddle.right < self.settings.SCREEN_WIDTH:
            self.paddle.x += self.settings.SCREEN_WIDTH // 100

    def draw_objects(self):
        """Nesneleri ekrana çizer."""
        screen.fill(self.settings.COLORS["white"])
        screen.blit(self.ball_image, (self.ball.x, self.ball.y))
        pygame.draw.rect(screen, self.settings.COLORS["blue"], self.paddle)  # Paddle
        self.update_score()

    def update_score(self):
        """Skoru ekrana yazdırır."""
        score_text = FONT.render(
            f"Score: {self.score}", True, self.settings.COLORS["black"]
        )
        screen.blit(score_text, (10, 10))

    def game_over(self):
        screen.fill(self.settings.COLORS["white"])
        game_over_text = FONT.render(
            f"Game Over! Score: {self.score}", True, self.settings.COLORS["black"]
        )
        screen.blit(
            game_over_text,
            (self.settings.SCREEN_WIDTH // 2 - 100, self.settings.SCREEN_HEIGHT // 2),
        )
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    def run(self):
        """Oyun döngüsü."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Paddle ve top hareketlerini kontrol et
            self.handle_paddle_movement()
            self.ball.x += self.ball_speed[0]
            self.ball.y += self.ball_speed[1]
            self.handle_collisions()

            # Nesneleri ekrana çiz
            self.draw_objects()
            pygame.display.flip()

            # FPS'yi ayarla
            clock.tick(self.settings.FPS)


# Oyunu başlat
if __name__ == "__main__":
    game = TikTakBallGame()
    game.run()
