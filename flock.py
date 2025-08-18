from imports import *
from settings import Settings
from functions import *
from boid import Boid


class Flock:
    '''
    '''

    def __init__(self, settings: Settings):
        self.agents = []
        self.settings = settings
        self.default_agent_position = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)
        for _ in range(10):
            a = Boid(15, self.settings.BOID_COLOR, self.default_agent_position)
            self.agents.append(a)

        

    def update_flock(self, screen: pygame.Surface) -> None:
        '''
        Update all agents on screen 
        Draws agents onto Screen surface
        '''
        for agent in self.agents:
                self.random_movement(agent)
                self.check_screen_margin(agent)
                agent.draw_boid(screen)


    def random_movement(self, agent: Boid) -> None:
        '''
        Randomly steer a single agent into a random direction
        as well as alter agents speed
        '''
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
        

    def check_screen_margin(self, agent: Boid) -> None:
        ''' 
        Adjusts the agent's angle to steer it away from the screen bounds.
        This function detects if the agent is too close to the screen edges 
        and modifies its angle based on its position and current direction.
        '''
        agent_pos = agent.get_position()
        agent_angle = agent.get_angle()

        # Check Top of Screen
        if int(agent_pos.y) < self.settings.SCREEN_MARGIN:
            if agent_angle >= 0 and agent_angle <= 135:  # Pointing up or right
                agent.update_angle(3)
                return
            elif agent_angle >= 225 and agent_angle < 360:  # Pointing left
                agent.update_angle(-3)
                return

        # Check Bottom of Screen
        elif int(agent_pos.y) > (self.settings.HEIGHT - self.settings.SCREEN_MARGIN):
            if agent_angle >= 45 and agent_angle <= 180:  # Pointing down or right
                agent.update_angle(-3)
                return
            elif agent_angle <= 315 and agent_angle > 180:  # Pointing left
                agent.update_angle(3)
                return

        # Check Left of Screen
        if int(agent_pos.x) < self.settings.SCREEN_MARGIN:
            if agent_angle >= 270 or agent_angle <= 45:  # Pointing left or up
                agent.update_angle(3)
                return
            elif agent_angle < 270 and agent_angle >= 135:  # Pointing down
                agent.update_angle(-3)
                return

        # Check Right of Screen
        elif int(agent_pos.x) > (self.settings.WIDTH - self.settings.SCREEN_MARGIN):
            if agent_angle >= 315 or agent_angle <= 90:  # Pointing right or up
                agent.update_angle(-3)
                return
            elif agent_angle <= 225 and agent_angle > 90:  # Pointing down
                agent.update_angle(3)
                return

    # Placeholder methods for future implementation
    def separation(self) -> None:
        '''Handle separation behavior (to be implemented).'''
        pass

    def alignment(self) -> None:
        '''Handle alignment behavior (to be implemented).'''
        pass

    def cohesion(self) -> None:
        '''Handle cohesion behavior (to be implemented).'''
        pass

    