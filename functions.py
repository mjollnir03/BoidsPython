from imports import * 
import settings
from boid import Boid

'''
Function to deter agents away from screen bounds automatically 
''' 
def check_screen_margin(agent: Boid) -> None:
    
    agent_pos = agent.get_position()
    agent_angle = agent.get_angle()

    # Check Top of Screen
    if int(agent_pos.y) < settings.SCREEN_MARGIN:   
        # if pointing up or right
        if agent_angle >= 0 and  agent_angle <= 135:
            agent.update_angle(3)
            return

        # If agent pointing left 
        elif agent_angle >= 225 and agent_angle < 360:
            agent.update_angle(-3)
            return

    # Check Bottom of Screen
    elif int(agent_pos.y) > (settings.HEIGHT - settings.SCREEN_MARGIN):
        # if pointing down or right
        if agent_angle >= 45 and agent_angle <= 180:
            agent.update_angle(-3)
            return

        # if pointing left
        elif agent_angle <= 315 and agent_angle > 180:
            agent.update_angle(3)
            return

    # Check Left of Screen
    if int(agent_pos.x) < settings.SCREEN_MARGIN:
        # if pointing left or up
        if agent_angle >= 270 or agent_angle <= 45:
            agent.update_angle(3)
            return

        # if pointing down
        elif agent_angle < 270 and agent_angle >= 135:
            agent.update_angle(-3)
            return
    
    # Check Right of Screen
    elif int(agent_pos.x) > (settings.WIDTH - settings.SCREEN_MARGIN):
        # if pointing right or up
        if agent_angle >= 315 or agent_angle <= 90:
            agent.update_angle(-3)
            return
        # if pointing down
        elif agent_angle <= 225 and agent_angle > 90:
            agent.update_angle(3)
            return
        

'''
Function to give multi-directional movement to a specific agent
'''
def get_user_input(keys, agent: Boid) -> None:
    if keys[pygame.K_w]:  # Increase speed (forward)
        agent.set_speed(min(agent.get_speed() + 0.1, 5))  # Max speed of 5
        
    if keys[pygame.K_s]:  # Decrease speed (reverse)
        agent.set_speed(max(agent.get_speed() - 0.1, 0.1))  # Minimum Speed is 0 (Stationary)
        
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
    return settings.FPS_FONT.render(f"FPS: {int(settings.CLOCK.get_fps())}", 0, settings.BOID_COLOR)


'''
Function to Check if Window Size is Beyond Allowed Minimum Limit
'''
def check_window_resize(event) -> None:
    settings.WIDTH, settings.HEIGHT = event.size  # Get new width and height from the resize event
    if settings.WIDTH < 600:
        settings.WIDTH = 600
    if settings.HEIGHT < 400:
        settings.HEIGHT = 400
    settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
    