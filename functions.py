from imports import *
import settings
from boid import Boid

def check_screen_margin(agent: Boid) -> bool:
    ''' 
    Adjusts the agent's angle to steer it away from the screen bounds.
    This function detects if the agent is too close to the screen edges 
    and modifies its angle based on its position and current direction.
    '''
    agent_pos = agent.get_position()
    agent_angle = agent.get_angle()

    # Check Top of Screen
    if int(agent_pos.y) < settings.SCREEN_MARGIN:
        if agent_angle >= 0 and agent_angle <= 135:  # Pointing up or right
            agent.update_angle(3)
            return
        elif agent_angle >= 225 and agent_angle < 360:  # Pointing left
            agent.update_angle(-3)
            return

    # Check Bottom of Screen
    elif int(agent_pos.y) > (settings.HEIGHT - settings.SCREEN_MARGIN):
        if agent_angle >= 45 and agent_angle <= 180:  # Pointing down or right
            agent.update_angle(-3)
            return
        elif agent_angle <= 315 and agent_angle > 180:  # Pointing left
            agent.update_angle(3)
            return

    # Check Left of Screen
    if int(agent_pos.x) < settings.SCREEN_MARGIN:
        if agent_angle >= 270 or agent_angle <= 45:  # Pointing left or up
            agent.update_angle(3)
            return
        elif agent_angle < 270 and agent_angle >= 135:  # Pointing down
            agent.update_angle(-3)
            return

    # Check Right of Screen
    elif int(agent_pos.x) > (settings.WIDTH - settings.SCREEN_MARGIN):
        if agent_angle >= 315 or agent_angle <= 90:  # Pointing right or up
            agent.update_angle(-3)
            return
        elif agent_angle <= 225 and agent_angle > 90:  # Pointing down
            agent.update_angle(3)
            return


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


def get_fps() -> str:
    ''' 
    Renders the current FPS as a text surface.
    This function retrieves the FPS count from the clock 
    and creates a rendered surface to display it on the screen.
    '''
    return settings.FPS_FONT.render(f"FPS: {int(settings.CLOCK.get_fps())}", 0, settings.BOID_COLOR)


def check_window_resize(event) -> None:
    ''' 
    Handles resizing of the game window.
    Ensures the resized window does not go below a minimum width and height,
    and updates the settings accordingly.
    '''
    settings.WIDTH, settings.HEIGHT = event.size  # Get new width and height from the resize event
    if settings.WIDTH < 600:
        settings.WIDTH = 600
    if settings.HEIGHT < 400:
        settings.HEIGHT = 400
    settings.SCREEN = pygame.display.set_mode(
        (settings.WIDTH, settings.HEIGHT),
        pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
    )

def random_movement(agent: Boid) -> None:
    rv1 = random.randint(1,4)
    rv2 = random.randint(1,4)

    if rv1 != rv2:
        return

    if rv1 == rv2 == 1:  # Increase speed (forward)
        agent.set_speed(min(agent.get_speed() + 0.2, 5))  # Max speed of 5

    elif rv1 == rv2 == 2:  # Decrease speed (reverse)
        agent.set_speed(max(agent.get_speed() - 0.2, 0.2))  # Minimum speed is 0.1 (Stationary)

    elif rv1 == rv2 == 3:  # Rotate left
        agent.update_angle(-5)  # Rotate left by 3 degrees

    elif rv1 == rv2 == 4:  # Rotate right
        agent.update_angle(5)  # Rotate right by 3 degrees
