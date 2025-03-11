import pygame
from ball import Ball
from logic import (
    add_ball, update_balls, check_ball_collisions, generate_blocks, update_blocks,
    check_block_collisions, get_current_color
)
from ui import start_menu, pause_menu, end_menu, draw_text

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls Game")

# Clock
clock = pygame.time.Clock()

def main():
    running = True
    paused = False
    game_over = False
    balls = []
    dt = 0  # Time since last frame in milliseconds

    while running:
        if not game_over:
            if not paused:
                screen.fill((255, 255, 255))  # Clear screen

                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        balls.append(add_ball(x, y))
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = not paused

                # Update game state
                update_balls(balls, dt)
                balls = check_ball_collisions(balls)
                generate_blocks()
                update_blocks()
                check_block_collisions(balls)

                # Draw all game objects
                for ball in balls:
                    ball.draw(screen)
                for block in blocks:
                    block.draw(screen)

                # Display current global color
                current_color = get_current_color()
                draw_text(screen, f"Current Color: {current_color}", 24, 100, 20, current_color)

                # Check for win condition
                if len(balls) == 1:
                    game_over = True
                    winner = balls[0].color

                pygame.display.flip()
                dt = clock.tick(60)  # Cap at 60 FPS
            else:
                # Pause menu
                pause_menu(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p:
                            paused = not paused
                        elif event.key == pygame.K_q:
                            running = False
        else:
            # End menu
            end_menu(screen, winner)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()  # Restart the game
                    elif event.key == pygame.K_q:
                        running = False

    pygame.quit()

if __name__ == "__main__":
    start_menu(screen)
    main()