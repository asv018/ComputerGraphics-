import pygame
import math

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Unlock Clock')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock_center = (screen_width // 2, screen_height // 2)
clock_radius = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, clock_center, clock_radius, 2)

    start_point = (clock_center[0] - clock_radius //
                   2, clock_center[1] + clock_radius // 3)
    middle_point = (clock_center[0] - clock_radius //
                    4, clock_center[1] + clock_radius // 2)
    end_point = (clock_center[0] + clock_radius // 3,
                 clock_center[1] - clock_radius // 4)
    pygame.draw.line(screen, BLACK, start_point, middle_point, 2)
    pygame.draw.line(screen, BLACK, middle_point, end_point, 2)

    pygame.display.update()

pygame.quit()
