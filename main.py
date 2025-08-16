from imports import *
import settings
from boid import Boid
from functions import *

# # Initialize the boids at the center
agent_position = (settings.WIDTH // 2, settings.HEIGHT // 2)

# Create 10 Boid Agents 
agents = list()

for i in range(10):
    a = Boid(15, settings.BOID_COLOR, agent_position)
    agents.append(a)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE: 
            check_window_resize(event)

    settings.WIDTH, settings.HEIGHT = settings.SCREEN.get_size()

    # Fill the screen with the background color
    settings.SCREEN.fill(settings.SCREEN_BACKGROUND_COLOR)

    for agent in agents:
        random_movement(agent)
        check_screen_margin(agent)
        agent.draw_boid()
    

    # Display FPS 
    settings.SCREEN.blit(get_fps(), (0, 0))
    
    # Update the display
    pygame.display.flip()    
    
    # Limit the frame rate
    settings.CLOCK.tick(60)