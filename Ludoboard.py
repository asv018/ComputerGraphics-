import pygame

# Initialize Pygame
pygame.init()

# Constants for colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Define the Ludo board dimensions
board_width = 600
board_height = 600

# Initialize the screen
screen = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Ludo Board")

# Function to draw the Ludo board


def draw_ludo_board(screen):
    # Draw the outer square
    pygame.draw.rect(screen, WHITE, (50, 50, 500, 500))

    # Draw the home columns (squares)
    for i in range(4):
        pygame.draw.rect(screen, GREEN, (75 + i * 100, 75, 50, 425))

    for i in range(4):
        pygame.draw.rect(screen, RED, (75, 75 + i * 100, 425, 50))

    for i in range(4):
        pygame.draw.rect(screen, YELLOW, (525 - i * 100, 75, 50, 425))

    for i in range(4):
        pygame.draw.rect(screen, BLUE, (75, 525 - i * 100, 425, 50))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the Ludo board
    draw_ludo_board(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
