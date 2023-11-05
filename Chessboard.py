import pygame

# Initialize Pygame
pygame.init()

# Constants for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the chessboard dimensions
board_width = 8
board_height = 8
square_size = 50  # Size of each square in pixels

# Initialize the screen
screen = pygame.display.set_mode(
    (board_width * square_size, board_height * square_size))
pygame.display.set_caption("Chessboard")

# Function to draw the chessboard


def draw_chessboard(screen):
    for row in range(board_height):
        for col in range(board_width):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * square_size,
                             row * square_size, square_size, square_size))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the chessboard
    draw_chessboard(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
