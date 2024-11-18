from imports import *
import settings
from boid import Boid
from functions import *


# Initialize the boid at the center
agent1_position = (WIDTH // 2, HEIGHT // 2)
agent1 = Boid(25, BOID_COLOR, agent1_position)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            
            WIDTH, HEIGHT = event.size  # Get new width and height from the resize event
            if WIDTH < 600:
                WIDTH = 600
            if HEIGHT < 400:
                HEIGHT = 400
            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)

    WIDTH, HEIGHT = SCREEN.get_size()
    print(id(HEIGHT) ,id(WIDTH))

    # Get user input and update Boid
    keys = pygame.key.get_pressed()
    get_user_input(keys, agent1)
    
    # Check for screen margins and adjust Boid's angle if necessary
    check_screen_margin(agent1)
    
    # Update the boid's position based on speed and direction
    agent1.update_position()
    
    # Fill the screen with the background color
    SCREEN.fill(SCREEN_BACKGROUND_COLOR)
    
    # Draw the boid
    agent1.draw_boid(SCREEN)
    
    
    # Display FPS (assuming you have a function get_fps() defined)
    SCREEN.blit(get_fps(), (0, 0))
    
    # Update the display
    pygame.display.flip()
    
    
    
    
    # Limit the frame rate
    CLOCK.tick(60)