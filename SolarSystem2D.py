import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Solar System')

sun_radius = 40
planet_data = [
    {"name": "Mercury", "radius": 10, "distance": 100, "color": YELLOW},
    {"name": "Venus", "radius": 15, "distance": 150, "color": ORANGE},
    {"name": "Earth", "radius": 15, "distance": 200, "color": BLUE},
    {"name": "Mars", "radius": 12, "distance": 250, "color": RED},
]

running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.draw.circle(screen, YELLOW, (screen_width //
                       2, screen_height // 2), sun_radius)

    for planet in planet_data:
        x = screen_width // 2 + \
            planet["distance"] * math.cos(math.radians(angle))
        y = screen_height // 2 + \
            planet["distance"] * math.sin(math.radians(angle))
        pygame.draw.circle(
            screen, planet["color"], (int(x), int(y),), planet["radius"])
        angle += 1  # Rotate the planets

    pygame.display.update()

pygame.quit()
