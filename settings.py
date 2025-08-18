from imports import *

@dataclass
class Settings():
    # BEHAVIOR STATS
    NUM_BOIDS = 500
    VISUAL_RANGE = 50
    PROTECTED_RANGE = 10
    AVOID_FACTOR = 0.05
    ALIGN_FACTOR = 0.05 
    COHESION_FACTOR = 0.0005

    # COLORS
    BOID_COLOR = (255, 255, 255)
    SCREEN_BACKGROUND_COLOR = (0,0,0)

    # FONTS
    FPS_FONT = pygame.font.SysFont("Arial" , 18 ) 

    # DISPLAY SETUP
    # ICON = pygame.image.load("")
    # pygame.display.set_icon()
    pygame.display.set_caption("Flocking Simulation") 
    DISPLAY_INFO = pygame.display.Info() 

    SCREEN_MARGIN = 25
    WIDTH, HEIGHT = 640, 480

    CLOCK = pygame.time.Clock()