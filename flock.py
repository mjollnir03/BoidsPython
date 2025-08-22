from imports import *
from settings import Settings
from functions import *
from boid import Boid


class Flock:
    '''
    Manages a collection of Boids and applies flocking rules each update.
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
                self.__random_movement(agent)

                # Apply 3 Rules only when agent is within screen bounds
                if not self.__check_screen_margin(agent):
                    self.__separation(agent)
                    self.__alignment(agent)
                    self.__cohesion(agent)

                agent.draw_boid(screen)


    def __random_movement(self, agent: Boid) -> None:
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
            agent.update_angle(-3)  # Rotate left by 3 degrees

        elif rv1 == rv2 == 4:  # Rotate right
            agent.update_angle(3)  # Rotate right by 3 degrees
        

    def __check_screen_margin(self, agent: Boid) -> bool:
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
                return True
            elif agent_angle >= 225 and agent_angle < 360:  # Pointing left
                agent.update_angle(-3)
                return True 

        # Check Bottom of Screen
        elif int(agent_pos.y) > (self.settings.HEIGHT - self.settings.SCREEN_MARGIN):
            if agent_angle >= 45 and agent_angle <= 180:  # Pointing down or right
                agent.update_angle(-3)
                return True
            elif agent_angle <= 315 and agent_angle > 180:  # Pointing left
                agent.update_angle(3)
                return True

        # Check Left of Screen
        if int(agent_pos.x) < self.settings.SCREEN_MARGIN:
            if agent_angle >= 270 or agent_angle <= 45:  # Pointing left or up
                agent.update_angle(3)
                return True
            elif agent_angle < 270 and agent_angle >= 135:  # Pointing down
                agent.update_angle(-3)
                return True

        # Check Right of Screen
        elif int(agent_pos.x) > (self.settings.WIDTH - self.settings.SCREEN_MARGIN):
            if agent_angle >= 315 or agent_angle <= 90:  # Pointing right or up
                agent.update_angle(-3)
                return True
            elif agent_angle <= 225 and agent_angle > 90:  # Pointing down
                agent.update_angle(3)
                return True
        
        return False

    def __separation(self, agent: Boid) -> None:
        """
        Steer the boid away from others that are too close.
        Implements the "separation" rule of flocking:
        - If neighbors are within PROTECTED_RANGE, push away.
        - Strength of push is scaled by AVOID_FACTOR.
        - Turn is limited by max_turn for smooth motion.
        """
        # Current position of this boid
        pos: Vector2 = agent.get_position()

        # Accumulated "push-away" vector (starts at zero)
        close = Vector2(0, 0)

        # Cache squared protected range (avoids sqrt for speed)
        pr = self.settings.PROTECTED_RANGE
        pr2 = pr * pr

        # Check all other boids in the flock
        for other in self.agents:
            if other is agent:
                continue  # skip self

            # Vector from neighbor -> this boid
            off = pos - other.get_position()

            # If neighbor is inside the protected range, add its offset
            if 0 < off.length_squared() < pr2:
                close += off  # accumulate push-away direction

        # Only steer if we actually found close neighbors
        if close.length_squared() > 0:
            # Desired heading = current direction + scaled away vector
            desired_dir = agent.get_direction() + close * self.settings.AVOID_FACTOR

            # Safety check: if vector collapses to (0,0), skip
            if desired_dir.length_squared() == 0:
                return

            # Normalize -> only direction matters
            desired_dir = desired_dir.normalize()

            # Convert desired direction into angle (relative to boid's 0 degree = (0, -1))
            base = Vector2(0, -1)
            desired_angle = base.angle_to(desired_dir)
            current_angle = agent.get_angle()

            # Compute smallest signed turn difference (range: -180 degree to +180 degree)
            delta = (desired_angle - current_angle + 180) % 360 - 180

            # Limit turning speed to keep motion smooth (no snapping)
            max_turn = 5  # degrees per update frame
            turn = max(-max_turn, min(max_turn, delta))

            # Apply turn adjustment to the boid
            agent.update_angle(turn)


        

    def __alignment(self, agent: Boid) -> None:
        '''Handle alignment behavior (to be implemented).'''
        pass

    def __cohesion(self, agent: Boid) -> None:
        '''Handle cohesion behavior (to be implemented).'''
        pass

    