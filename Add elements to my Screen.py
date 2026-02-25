import pygame
pygame.init()

width, height = 640, 480
caption = 'My first game screen'
bg_color = (255, 255, 255)  
rect_color = (255, 0, 0)    
text_color = (0, 0, 0)      
text_content = "Hello Pygame!"

# Create the display window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(caption)


rect_width, rect_height = 100, 50
rect_x = (width - rect_width) // 2
rect_y = (height - rect_height) // 2
center_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


font = pygame.font.Font(None, 36)
text_surface = font.render(text_content, True, text_color)
text_rect = text_surface.get_rect(center=(width // 2, height // 2+110))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(bg_color)
    pygame.draw.rect(screen, rect_color, center_rect)
    screen.blit(text_surface, text_rect)
    
    
    pygame.display.flip()


pygame.quit()