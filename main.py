from settings import *
from boid import Boid

# Initialize pygame
pygame.init()


#icon = pygame.image.load()
pygame.display.set_caption("Flocking Simulation")

# Set up display information and print the current screen resolution
displayInfo = pygame.display.Info()
print("Screen resolution:", displayInfo.current_w, "x", displayInfo.current_h)

# Set up screen and clock
screen = pygame.display.set_mode((640, 480), HWSURFACE | DOUBLEBUF | RESIZABLE | DOUBLEBUF)  # Initial screen size 640x480, resizable
clock = pygame.time.Clock()  # Create a clock to control frame rate

width, height = 640, 480

# Create a surface for the triangle
triangle_surface = pygame.Surface((100, 100), pygame.SRCALPHA)  # 200x200 with transparency
triangle_points = [(50, 0), (100, 100), (0, 100)]  # Centered triangle within the surface
pygame.draw.polygon(triangle_surface, (255,0,0), triangle_points)

angle = 0.0

# Run window
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == VIDEORESIZE:
            width, height = event.size  # Get new width and height from the resize event
            if width < 600:  # Enforce minimum width of 600
                width = 600
            if height < 400:  # Enforce minimum height of 400
                height = 400
            screen = pygame.display.set_mode((width, height), HWSURFACE | DOUBLEBUF | RESIZABLE)  # Resize screen

    # Fill the screen with black (background color)
    screen.fill(SCREEN_BACKGROUND_COLOR)
    
    rotated_triangle = pygame.transform.rotate(triangle_surface, angle)

    # Draw Tringle 
    screen.blit(rotated_triangle, rotated_triangle.get_rect(center=(width/2,height/2)))
    
    angle += 5.0
    # Update display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit pygame after closing window
pygame.quit()
