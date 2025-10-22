import pygame, sys, random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid Obstacles")
icon = pygame.image.load("Car3.png")   
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Car
player_img = pygame.image.load("Car3.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (80, 80))
player_rect = player_img.get_rect(center=(WIDTH- 2, HEIGHT - 80))
player_speed = 6

# Obstacle
obstacle_img = pygame.image.load("obstacle1.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (30, 40))
obstacle = obstacle_img.get_rect(center=(random.randint(50, WIDTH - 50), -100))
obstacle_speed = 4

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Main loop
while True:
    # 1. Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += player_speed

    # 3. Move obstacle
    obstacle.y += obstacle_speed
    if obstacle.top > HEIGHT:
        obstacle.y = -100
        obstacle.x = random.randint(0, WIDTH - 50)
        score += 1
        obstacle_speed += 0.3

    # 4. Collision detection
    if player_rect.colliderect(obstacle):
        screen.fill(WHITE)
        screen.blit(player_img, player_rect)
        screen.blit(obstacle_img, obstacle)
        game_over_text = font.render("GAME OVER!", True, (0, 0, 255))
        score_text = font.render(f"Your Score: {score}", True, (0, 0, 255))
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 40))
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    

    # 5. Draw everything
    screen.fill(WHITE)
    screen.blit(player_img, player_rect)
    screen.blit(obstacle_img, obstacle)
    text = font.render(f"Score: {score}", True,(0, 0, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

