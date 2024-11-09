
from settings import *

class Boid:
    def __init__(self, size: int, color: Tuple[int, int, int], position: List[int]):
        self.angle = 0
        self.size = size
        self.color = color
        self.position = Vector2(position)  # Use Vector2 for position
        self.direction = Vector2(0, -1)  # Initially up
        self.speed = 0  # Initial speed
        self.calculate_dimensions()

        # Create the base surface for the boid
        self.base_surface = pygame.Surface((self.size, self.height), pygame.SRCALPHA)
        pygame.draw.polygon(self.base_surface, self.color, self.triangle_points)

    def calculate_dimensions(self) -> None:
        self.base = self.size
        self.height = ceil(self.base * 1.75)  # Adjust height as needed for an isosceles triangle
        self.triangle_points = [
            (self.size // 2, 0),         # Top point
            (self.size, self.height),    # Bottom-right corner
            (0, self.height)             # Bottom-left corner
        ]

    def update_position(self) -> None:
        # Update position based on the direction and speed
        self.position += self.direction * self.speed

    def update_angle(self, angle_offset: int) -> None:
        # Adjust angle and rotate direction vector
        self.angle += angle_offset
        self.angle %= 360  # Keep angle within 0-359 degrees
        self.direction = Vector2(0, -1).rotate(self.angle)  # Update direction based on angle

    def draw_boid(self, screen) -> None:
        # Rotate the base surface to match the current angle
        rotated_surface = pygame.transform.rotate(self.base_surface, -self.angle)
        rotated_rect = rotated_surface.get_rect(center=(self.position.x, self.position.y))

        # Draw the rotated surface to the screen
        screen.blit(rotated_surface, rotated_rect)

        # Optional: draw a rectangle outline around the boid for debugging
        pygame.draw.rect(screen, (0, 255, 0), rotated_rect, 1)