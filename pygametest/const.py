"""
Constant types in Python.
"""
import pygame
from pygame.locals import *

class _const:
    class ConstError(TypeError):
        pass

    def __init__(self):
        self.SCREEN_SIZE = (600, 400)
        self.BACKGROUND = (153, 204, 0)
        self.BLACK = (0, 0, 0)
        self.KEY_TIMER = K_LEFT

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()