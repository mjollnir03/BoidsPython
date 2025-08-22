from imports import *
from settings import Settings
from functions import *
from flock import Flock

class Main:
    '''
    Program entry point and simulation loop.
    '''
    
    def __init__(self): 
        # 
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.flock = Flock(self.settings)

    def run(self) -> None:
        # Main Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.VIDEORESIZE: 
                    self.__check_window_resize(event)

            # Fill the screen with the background color
            self.screen.fill(self.settings.SCREEN_BACKGROUND_COLOR)

            # Update Flock of Boids
            self.flock.update_flock(self.screen)
            
            # Display FPS 
            self.screen.blit(self.__get_fps(), (0, 0))
            
            # Update the display
            pygame.display.flip()    
            
            # Limit the frame rate
            self.settings.CLOCK.tick(60)


    def __get_fps(self) -> str:
        ''' 
        Renders the current FPS as a text surface.
        This function retrieves the FPS count from the clock 
        and creates a rendered surface to display it on the screen.
        '''
        return self.settings.FPS_FONT.render(f"FPS: {int(self.settings.CLOCK.get_fps())}", 0, self.settings.BOID_COLOR)


    def __check_window_resize(self, event: pygame.event.Event,) -> None:
        ''' 
        Handles resizing of the game window.
        Ensures the resized window does not go below a minimum width and height,
        and updates the settings accordingly.
        '''
        self.settings.WIDTH, self.settings.HEIGHT = event.size  # Get new width and height from the resize event
        if self.settings.WIDTH < 600:
            self.settings.WIDTH = 600
        if self.settings.HEIGHT < 400:
            self.settings.HEIGHT = 400
        self.screen = pygame.display.set_mode(
            (self.settings.WIDTH, self.settings.HEIGHT),
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
        )

        self.settings.WIDTH, self.settings.HEIGHT = self.screen.get_size()

    

# Start Simulation
main = Main()
main.run()