import random
import math
from ball import Ball

# Game state variables
global_current_color = (255, 255, 255)
color_change_timer = 0
blocks = []

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.timer = 900  # 15 seconds at 60 FPS
        self.size = 25

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

def add_ball(x, y):
    radius = 20
    color = global_current_color
    dx = random.choice([-4, 4])
    dy = random.choice([-4, 4])
    return Ball(x, y, radius, color, dx, dy)

def update_global_color(dt):
    global color_change_timer, global_current_color
    color_change_timer += dt
    if color_change_timer >= 10000:  # 10 seconds
        global_current_color = (random.randint(0, 255), 
                               random.randint(0, 255), 
                               random.randint(0, 255))
        color_change_timer = 0

def update_balls(balls, dt):
    for ball in balls:
        ball.move()
        # Update ball color to match global color
        ball.color = global_current_color

def check_ball_collisions(balls):
    new_balls = []
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if balls[i].collides_with(balls[j]):
                # Only shrink if colors are different
                if balls[i].color != balls[j].color:
                    balls[i].shrink()
                    balls[j].shrink()
    
    return [ball for ball in balls if ball.radius >= 5]

def generate_blocks():
    # 1% chance to spawn block each frame
    if random.random() < 0.01:
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        # Generate random color different from current global color
        block_color = global_current_color
        while block_color == global_current_color:
            block_color = (random.randint(0, 255), 
                         random.randint(0, 255), 
                         random.randint(0, 255))
        blocks.append(Block(x, y, block_color))

def update_blocks():
    global blocks
    # Update block timers
    for block in blocks:
        block.timer -= 1
    
    # Remove expired blocks
    blocks = [block for block in blocks if block.timer > 0]

def check_block_collisions(balls):
    global blocks
    for ball in balls:
        for block in blocks[:]:
            # Simple AABB collision detection
            if (ball.x + ball.radius > block.x and
                ball.x - ball.radius < block.x + block.size and
                ball.y + ball.radius > block.y and
                ball.y - ball.radius < block.y + block.size):
                
                # Change direction
                ball.dx *= -1
                ball.dy *= -1
                
                # Damage ball if colors don't match
                if block.color != ball.color:
                    ball.shrink()
                
                # Remove block
                blocks.remove(block)
                break

def get_current_color():
    return global_current_color