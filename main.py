# Ellmaer Ranjber

import pygame  # Import pygame (SDL)

pygame.init()  # Initialize pygame

# Set up display information
displayInfo = pygame.display.Info()
print(displayInfo.current_w, displayInfo.current_h)

# Set up screen and clock
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
clock = pygame.time.Clock()  # Create a clock to control frame rate

# Run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update display
    pygame.display.flip()

    print(screen.get_size())

    # Limit to 30 frames per second
    clock.tick(5)

# Quit pygame after closing window
pygame.quit()
