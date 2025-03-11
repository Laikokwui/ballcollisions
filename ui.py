import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_text(screen, text, size, x, y, color):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def start_menu(screen):
    screen.fill(WHITE)
    draw_text(screen, "Bouncing Balls Game", 64, 400, 200, BLACK)
    draw_text(screen, "Click to Add Balls", 48, 400, 350, BLUE)
    draw_text(screen, "Press Q to Quit", 48, 400, 400, RED)
    pygame.display.flip()

def pause_menu(screen):
    screen.fill(WHITE)
    draw_text(screen, "Paused", 64, 400, 200, BLACK)
    draw_text(screen, "Press P to Resume", 48, 400, 350, BLUE)
    draw_text(screen, "Press Q to Quit", 48, 400, 400, RED)
    pygame.display.flip()

def end_menu(screen, winner):
    screen.fill(WHITE)
    draw_text(screen, f"Ball with Color {winner} Wins!", 64, 400, 200, BLACK)
    draw_text(screen, "Press R to Replay", 48, 400, 350, BLUE)
    draw_text(screen, "Press Q to Quit", 48, 400, 400, RED)
    pygame.display.flip()