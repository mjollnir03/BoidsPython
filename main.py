from imports import *
import settings
from boid import Boid
from functions import *

# Initialize the boid at the center
agent1_position = (settings.WIDTH // 2, settings.HEIGHT // 2)
agent1 = Boid(25,settings.BOID_COLOR, agent1_position)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE: 
            check_window_resize(event)

    settings.WIDTH, settings.HEIGHT = settings.SCREEN.get_size()

    # Get user input and update Boid
    keys = pygame.key.get_pressed()
    get_user_input(keys, agent1)
    
    # Check for screen margins and adjust Boid's angle if necessary
    check_screen_margin(agent1)
    
    # Fill the screen with the background color
    settings.SCREEN.fill(settings.SCREEN_BACKGROUND_COLOR)
    
    # Draw the boid
    agent1.draw_boid()
    
    # Display FPS 
    settings.SCREEN.blit(get_fps(), (0, 0))
    
    # Update the display
    pygame.display.flip()    
    
    # Limit the frame rate
    settings.CLOCK.tick(60)