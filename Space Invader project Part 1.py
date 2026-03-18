import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")

class SpriteObject(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

# --- Setup Sprites ---
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

# Create the Player
player = SpriteObject(BLUE, 20, 20)
all_sprites_list.add(player)

# Create 7 Enemy Sprites in random positions
for i in range(7):
    enemy = SpriteObject(RED, 20, 20)
    enemy.rect.x = random.randrange(SCREEN_WIDTH - 20)
    enemy.rect.y = random.randrange(SCREEN_HEIGHT - 20)
    enemy_list.add(enemy)
    all_sprites_list.add(enemy)

# Game variables
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
running = True

# --- Main Game Loop ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement (Arrow Keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:  player.rect.x -= 5
    if keys[pygame.K_RIGHT]: player.rect.x += 5
    if keys[pygame.K_UP]:    player.rect.y -= 5
    if keys[pygame.K_DOWN]:  player.rect.y += 5

    # Collision Detection
    # spritecollide returns a list of enemies hit by the player
    hit_list = pygame.sprite.spritecollide(player, enemy_list, False)
    
    for enemy in hit_list:
        score += 1
        # Reposition enemy randomly after collision
        enemy.rect.x = random.randrange(SCREEN_WIDTH - 20)
        enemy.rect.y = random.randrange(SCREEN_HEIGHT - 20)
        print(f"Collision! Current Score: {score}")

    # Drawing
    screen.fill(WHITE)
    all_sprites_list.draw(screen)
    
    # Display Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
