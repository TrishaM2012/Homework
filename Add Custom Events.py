import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Event Color Change")
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

class ColorChangingSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self):
        new_color = random.choice(COLORS)
        while new_color == self.color:
            new_color = random.choice(COLORS)
        self.color = new_color
        self.image.fill(self.color)
        
sprite1 = ColorChangingSprite(COLORS[0], SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
sprite2 = ColorChangingSprite(COLORS[1], 3 * SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((30, 30, 30))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()