from settings import *
from boid import Boid



agent1 = Boid(25, (255,0,0), (WIDTH//2, HEIGHT//2))
agent1.calculate_dimensions()



angle = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == VIDEORESIZE:
            WIDTH, HEIGHT = event.size  # Get new width and height from the resize event
            if WIDTH < 600:  # Enforce minimum width of 600
                WIDTH = 600
            if HEIGHT < 400:  # Enforce minimum height of 400
                HEIGHT = 400
            SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)  # Resize screen

    # Fill the screen with black (background color)
    SCREEN.fill(SCREEN_BACKGROUND_COLOR)
    
    

    # Draw Tringle 
    agent1.draw_boid(SCREEN)

    # Update display
    pygame.display.flip()
    print(pygame.mouse.get_pos())

    # Limit frames per second
    CLOCK.tick(60)
