from imports import *
import settings
from boid import Boid


def get_user_input(keys, agent: Boid) -> None:
    ''' 
    Processes user keyboard input to control the agent.
    WASD keys adjust speed and rotation: 
    - W: Increase speed
    - S: Decrease speed
    - A: Rotate left
    - D: Rotate right
    '''
    if keys[pygame.K_w]:  # Increase speed (forward)
        agent.set_speed(min(agent.get_speed() + 0.1, 5))  # Max speed of 5

    if keys[pygame.K_s]:  # Decrease speed (reverse)
        agent.set_speed(max(agent.get_speed() - 0.1, 0.1))  # Minimum speed is 0.1 (Stationary)

    if keys[pygame.K_a]:  # Rotate left
        agent.update_angle(-3)  # Rotate left by 3 degrees

    if keys[pygame.K_d]:  # Rotate right
        agent.update_angle(3)  # Rotate right by 3 degrees



