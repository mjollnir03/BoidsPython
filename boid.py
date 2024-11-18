from imports import *
import settings

class Boid:
    def __init__(self, size: int, color: Tuple[int, int, int], position: Tuple[float, float]):
        self.__angle = 0
        self.__size = size
        self.__color = color
        self.__position = Vector2(position)
        self.__direction = Vector2(0, -1)  # Initially pointing up
        self.__speed = 0  # Initial speed
        self.__calculate_dimensions()

        # Create the base surface for the boid
        self.__base_surface = pygame.Surface((self.__size, self.__height), pygame.SRCALPHA)
        pygame.draw.polygon(self.__base_surface, self.__color, self.__triangle_points)

    def __calculate_dimensions(self) -> None:
        self.__base = self.__size
        self.__height = ceil(self.__base * 1.75)  # Adjust height as needed for an isosceles triangle
        self.__triangle_points = [
            (self.__size // 2, 0),         # Top point
            (self.__size, self.__height),  # Bottom-right corner
            (0, self.__height)             # Bottom-left corner
        ]

    def update_position(self) -> None:
        # Update position based on the direction and speed
        self.__position += self.__direction * self.__speed

    def set_position(self, position: Tuple[float, float]) -> None:
        self.__position = Vector2(position)

    def get_direction(self) -> Vector2:
        return self.__direction

    def get_position(self) -> Vector2:
        return self.__position

    def get_angle(self) -> float:
        return self.__angle

    def update_angle(self, angle_offset: float) -> None:
        # Adjust angle and rotate direction vector
        self.__angle += angle_offset
        self.__angle %= 360  # Keep angle within 0-359 degrees
        self.__direction = Vector2(0, -1).rotate(self.__angle)  # Update direction based on angle

    def draw_boid(self, screen) -> None:
        # Rotate the base surface to match the current angle
        rotated_surface = pygame.transform.rotate(self.__base_surface, -self.__angle)
        rotated_rect = rotated_surface.get_rect(center=(self.__position.x, self.__position.y))

        # Draw the rotated surface to the screen
        screen.blit(rotated_surface, rotated_rect)

        # Optional: Draw a rectangle around the boid for debugging
        pygame.draw.rect(screen, (255, 0, 0), rotated_rect, 1)

    def display_boid_metrics(self) -> None:
        print(f"Current Angle: {self.__angle}")
        print(f"Current Direction: {self.__direction}")
        print(f"Current Position: {self.__position}")
        print(f"Current Speed: {self.__speed}")
        print()

    def get_speed(self) -> float:
        return self.__speed

    def set_speed(self, speed: float) -> None:
        self.__speed = speed

    # Additional methods if needed
    def separation(self) -> None:
        pass

    def alignment(self) -> None:
        pass

    def cohesion(self) -> None:
        pass