import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 80, 80)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 36)

# Paddle settings
paddle_width = 120
paddle_height = 15
paddle_speed = 8

paddle = pygame.Rect(
    WIDTH // 2 - paddle_width // 2,
    HEIGHT - 50,
    paddle_width,
    paddle_height
)

# Ball settings
ball_radius = 12
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = -5

# Brick settings
brick_rows = 5
brick_cols = 10
brick_width = 70
brick_height = 25
brick_padding = 10
brick_offset_top = 60
brick_offset_left = 35

bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(
            brick_offset_left + col * (brick_width + brick_padding),
            brick_offset_top + row * (brick_height + brick_padding),
            brick_width,
            brick_height
        )
        bricks.append(brick)

# Score
score = 0


def draw_paddle():
    pygame.draw.rect(screen, BLUE, paddle)



def draw_ball():
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)



def draw_bricks():
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)



def show_score():
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 15))



def game_over(message):
    over_text = font.render(message, True, YELLOW)
    score_text = font.render(f"Final Score: {score}", True, WHITE)

    screen.fill(BLACK)

    screen.blit(over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 40))
    screen.blit(score_text, (WIDTH // 2 - 130, HEIGHT // 2 + 20))

    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()
    sys.exit()


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed

    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Wall collision
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x *= -1

    if ball_y - ball_radius <= 0:
        ball_speed_y *= -1

    # Paddle collision
    if paddle.collidepoint(ball_x, ball_y + ball_radius):
        ball_speed_y *= -1

    # Brick collision
    ball_rect = pygame.Rect(
        ball_x - ball_radius,
        ball_y - ball_radius,
        ball_radius * 2,
        ball_radius * 2
    )

    hit_index = ball_rect.collidelist(bricks)

    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed_y *= -1
        score += 10

    # Lose condition
    if ball_y > HEIGHT:
        game_over("GAME OVER")

    # Win condition
    if len(bricks) == 0:
        game_over("YOU WIN!")

    # Draw everything
    screen.fill(BLACK)

    draw_paddle()
    draw_ball()
    draw_bricks()
    show_score()

    pygame.display.update()
    clock.tick(FPS)
