# MODULE IMPORTS
import pygame
from pygame.locals import *
from math import atan2, degrees, ceil
import random
from typing import List, Tuple
from pygame.math import Vector2
from dataclasses import dataclass
# import numpy
# import threading
# import sys

# PYGAME INIT
if not pygame.get_init():
    pygame.init()

if not pygame.font.get_init():
    pygame.font.init()  
