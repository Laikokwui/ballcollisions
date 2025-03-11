import pygame

class Ball:
    def __init__(self, x, y, radius, color, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= 800:
            self.dx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= 600:
            self.dy *= -1

    def shrink(self):
        self.radius = max(5, self.radius - 5)  # Minimum radius of 5

    def collides_with(self, other):
        distance = ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        return distance <= self.radius + other.radius