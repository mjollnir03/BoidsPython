

from settings import *
from boid import Boid

# Initialize pygame
pygame.init()

# Set up display information and print the current screen resolution
displayInfo = pygame.display.Info()
print("Screen resolution:", displayInfo.current_w, "x", displayInfo.current_h)

# Set up screen and clock
screen = pygame.display.set_mode((640, 480), HWSURFACE | DOUBLEBUF | RESIZABLE)  # Initial screen size 640x480, resizable
clock = pygame.time.Clock()  # Create a clock to control frame rate

# Run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the loop to quit
        elif event.type == VIDEORESIZE:
            width, height = event.size  # Get new width and height from the resize event
            if width < 600:  # Enforce minimum width of 600
                width = 600
            if height < 400:  # Enforce minimum height of 400
                height = 400
            screen = pygame.display.set_mode((width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)  # Resize screen

    # Fill the screen with black (background color)
    screen.fill(SCREEN_BACKGROUND_COLOR)

    # Update display
    pygame.display.flip()

    # Print the current size of the screen after resizing
    print("Current screen size:", screen.get_size())

    # Limit frames per second
    clock.tick(5)

# Quit pygame after closing window
pygame.quit()
