# MODULE IMPORTS
import pygame
from pygame.locals import *
from math import ceil
import numpy
import threading
import random
import sys
from typing import List, Tuple
from pygame.math import Vector2

NUM_BOIDS = 500
VISUAL_RANGE = 50
PROTECTED_RANGE = 10
AVOID_FACTOR = 0.05
ALIGN_FACTOR = 0.05 
COHESION_FACTOR = 0.0005

# PYGAME INIT
pygame.init()
pygame.font.init()

# COLORS
BOID_COLOR = (255, 255, 255)
SCREEN_BACKGROUND_COLOR = (0,0,0)

# FONTS
FPS_FONT = pygame.font.SysFont("Arial" , 18 )

# DISPLAY SETUP
pygame.display.set_caption("Flocking Simulation") 
DISPLAY_INFO = pygame.display.Info()
print("Screen resolution:", DISPLAY_INFO.current_w, "x", DISPLAY_INFO.current_h)

SCREEN_MARGIN = 100

WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
CLOCK = pygame.time.Clock()  # Create a clock to control frame rate
