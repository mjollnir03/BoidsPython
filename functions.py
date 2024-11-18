from imports import * 
import settings
from boid import Boid


'''
Function to deter agents away from screen bounds automatically 
''' 
def check_screen_margin(agent: Boid) -> None:
    
    agent_pos = agent.get_position()
    agent_angle = agent.get_angle()

    print(id(HEIGHT), id(WIDTH))
    # Check Top of Screen
    if int(agent_pos.y) < 50:   
        # if pointing up or right
        if agent_angle >= 0 and  agent_angle <= 135:
            agent.update_angle(3)

        # If agent pointing left 
        elif agent_angle >= 225 and agent_angle < 360:
            agent.update_angle(-3)

    # Check Bottom of Screen
    if int(agent_pos.y) > (HEIGHT - 50):
        # if pointing down or right
        if agent_angle >= 45 and agent_angle <= 180:
            agent.update_angle(-3)

        # if pointing left
        elif agent_angle <= 315 and agent_angle > 180:
            agent.update_angle(3)

    # Check Left of Screen

    # Check Right of Screen
    
    pass



'''
Function to give multi-directional movement to a specific agent
'''
def get_user_input(keys, agent: Boid) -> None:
    if keys[pygame.K_w]:  # Increase speed (forward)
        agent.set_speed(min(agent.get_speed() + 0.1, 5))  # Max speed of 5
        
    if keys[pygame.K_s]:  # Decrease speed (reverse)
        agent.set_speed(max(agent.get_speed() - 0.1, 1))  # Max reverse speed of -3
        
    if keys[pygame.K_a]:  # Rotate left
        agent.update_angle(-3)  # Rotate left by 3 degrees
        
    if keys[pygame.K_d]:  # Rotate right
        agent.update_angle(3)  # Rotate right by 3 degrees

    # Optionally display boid metrics for debugging
    # agent.display_boid_metrics()

'''
Function to display FPS Count onto Screen
'''
# FPS Counter surface
def get_fps() -> str:
    return FPS_FONT.render(f"FPS: {int(CLOCK.get_fps())}", 0, BOID_COLOR)
