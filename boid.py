
from settings import *

class Boid:
    def __init__(self, size: int, color: Tuple[int, int, int], position: List[int]):
        self.size = size
        self.color = color
        self.position = position  # position[0] = x, position[1] = y

    def calculate_dimensions(self) -> None:
        self.base = self.size
        self.height = ceil(self.base * 1.75)  # Adjust height as needed for an isosceles triangle
        self.triangle_points = [
            (self.size // 2, 0), # Top point
            (self.size, self.height), # Bottom-right corner
            (0, self.height)          # Bottom-left corner
        ]

    def draw_boid(self, screen) -> None:
        # Create a temporary surface for the boid
        boid_surface = pygame.Surface((self.size, self.height), pygame.SRCALPHA)
        pygame.draw.polygon(boid_surface, self.color, self.triangle_points)
        boid_rect = boid_surface.get_rect(center=(self.position[0], self.position[1]))
        
        # Blit the boid surface to the main screen with center alignment
        screen.blit(boid_surface, boid_rect)
        pygame.draw.rect(screen, (0, 255, 0), boid_rect, 1) 
    

