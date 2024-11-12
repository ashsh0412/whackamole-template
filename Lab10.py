import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 640  # 20 squares * 32 pixels
WINDOW_HEIGHT = 512  # 16 squares * 32 pixels
SQUARE_SIZE = 32
GRID_COLS = 20
GRID_ROWS = 16

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")

# Load and scale the mole image
mole_image = pygame.image.load("mole.png")  # Make sure mole.png is in the same directory
mole_image = pygame.transform.scale(mole_image, (SQUARE_SIZE, SQUARE_SIZE))

# Initial mole position (top-left corner)
mole_x = 0
mole_y = 0

def draw_grid():
    """Draw the 20x16 grid of 32x32 squares"""
    # Draw vertical lines
    for x in range(0, WINDOW_WIDTH + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    
    # Draw horizontal lines
    for y in range(0, WINDOW_HEIGHT + 1, SQUARE_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

def move_mole_random():
    """Move the mole to a random grid position"""
    global mole_x, mole_y
    mole_x = random.randrange(0, GRID_COLS) * SQUARE_SIZE
    mole_y = random.randrange(0, GRID_ROWS) * SQUARE_SIZE

def is_mole_clicked(mouse_pos):
    """Check if the mouse click position overlaps with the mole"""
    mouse_x, mouse_y = mouse_pos
    mole_rect = pygame.Rect(mole_x, mole_y, SQUARE_SIZE, SQUARE_SIZE)
    return mole_rect.collidepoint(mouse_x, mouse_y)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if is_mole_clicked(event.pos):
                move_mole_random()
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the grid
    draw_grid()
    
    # Draw the mole
    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()