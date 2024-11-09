from settings import *
from boid import Boid

# Initialize the boid at the center
agent1Position = (WIDTH // 2, HEIGHT // 2)
agent1 = Boid(25, (255, 0, 0), agent1Position)

# FPS Counter surface
def get_fps() -> str:
    return FPS_FONT.render(f"FPS: {int(CLOCK.get_fps())}", 0, BOID_COLOR)

def get_user_input(keys, agent: Boid) -> None:
    if keys[pygame.K_w]:  # Increase speed (forward)
        agent.speed = min(agent.speed + 0.1, 5)  # Max speed of 5
        
    if keys[pygame.K_s]:  # Decrease speed (reverse)
        agent.speed = max(agent.speed - 0.1, -3)  # Max reverse speed of -3
        
    if keys[pygame.K_a]:  # Rotate left
        agent.update_angle(-3)  # Rotate left by 3 degrees
        
    if keys[pygame.K_d]:  # Rotate right
        agent.update_angle(3)  # Rotate right by 3 degrees
        
    #agent.display_boid_metrics()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == VIDEORESIZE:
            WIDTH, HEIGHT = event.size  # Get new width and height from the resize event
            if WIDTH < 600:
                WIDTH = 600
            if HEIGHT < 400:
                HEIGHT = 400
            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)

    get_user_input(pygame.key.get_pressed(), agent1)

    # Update the boid's position based on speed and direction
    agent1.update_position()

    # Fill the screen with the background color
    SCREEN.fill(SCREEN_BACKGROUND_COLOR)

    # Draw the boid
    agent1.draw_boid(SCREEN)

    # Display FPS
    SCREEN.blit(get_fps(), (0,0))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    CLOCK.tick(60)
