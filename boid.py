from imports import *

class Boid:
    '''
    Boid class to represent the Agents.
    Agents are isosceles triangles that move and rotate based on user input or other logic.
    '''
    
    def __init__(self, size: int, color: Tuple[int, int, int], position: Tuple[float, float]):
        '''Initialize the Boid with size, color, and position.'''
        self.__angle = 0
        self.__size = size
        self.__color = color
        self.__position = Vector2(position)
        self.__direction = Vector2(0, -1)  # Initially pointing up
        self.__speed = 0  # Initial speed
        self.__calculate_dimensions()
        self.__create_base_surface()

    def __calculate_dimensions(self) -> None:
        '''Calculate dimensions of the Boid's isosceles triangle.'''
        self.__base = self.__size
        self.__height = ceil(self.__base * 1.75)
        self.__triangle_points = [
            (self.__size // 2, 0),          # Top point
            (self.__size, self.__height),  # Bottom-right corner
            (0, self.__height)             # Bottom-left corner
        ]

    def __create_base_surface(self) -> None:
        '''Create the surface and draw the Boid's triangle shape.'''
        self.__base_surface = pygame.Surface((self.__size, self.__height), pygame.SRCALPHA)
        pygame.draw.polygon(self.__base_surface, self.__color, self.__triangle_points)

    def __update_position(self) -> None:
        '''Update the position of the Boid based on its speed and direction.'''
        self.__position += self.__direction * self.__speed

    def update_angle(self, angle_offset: float) -> None:
        '''
        Adjust the Boid's angle by a given offset.
        Updates the direction vector accordingly.
        '''
        self.__angle += angle_offset
        self.__angle %= 360  # Keep angle within 0-359 degrees
        self.__direction = Vector2(0, -1).rotate(self.__angle)

    def draw_boid(self, screen: pygame.Surface) -> None:
        '''Draw the Boid on the screen with its current rotation and position.'''
        self.__update_position()
        rotated_surface = pygame.transform.rotate(self.__base_surface, -self.__angle) # Negative Angle plugged in (refer to notes)
        rotated_rect = rotated_surface.get_rect(center=(self.__position.x, self.__position.y))
        screen.blit(rotated_surface, rotated_rect)

    # Getters and Setters
    def get_position(self) -> Vector2:
        '''Return the current position of the Boid.'''
        return self.__position

    def set_position(self, position: Tuple[float, float]) -> None:
        '''Set a new position for the Boid.'''
        self.__position = Vector2(position)

    def get_direction(self) -> Vector2:
        '''Return the current direction of the Boid.'''
        return self.__direction

    def get_angle(self) -> float:
        '''Return the current angle of the Boid.'''
        return self.__angle

    def get_speed(self) -> float:
        '''Return the current speed of the Boid.'''
        return self.__speed

    def set_speed(self, speed: float) -> None:
        '''Set a new speed for the Boid.'''
        self.__speed = speed
