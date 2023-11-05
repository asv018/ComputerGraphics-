import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Unlock Clock')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock center and radius
clock_center = (screen_width // 2, screen_height // 2)
clock_radius = 100

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the clock face
    pygame.draw.circle(screen, BLACK, clock_center, clock_radius, 2)

    # Draw the "unlocked" symbol (a checkmark)
    start_point = (clock_center[0] - clock_radius //
                   2, clock_center[1] + clock_radius // 3)
    middle_point = (clock_center[0] - clock_radius //
                    4, clock_center[1] + clock_radius // 2)
    end_point = (clock_center[0] + clock_radius // 3,
                 clock_center[1] - clock_radius // 4)
    pygame.draw.line(screen, BLACK, start_point, middle_point, 2)
    pygame.draw.line(screen, BLACK, middle_point, end_point, 2)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
