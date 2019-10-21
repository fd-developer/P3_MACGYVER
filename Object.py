import pygame
from pygame.locals import *


# Class in charge to manage objects as MacGyver, gardian, tools
class Object:

    def __init__(self, img, position):
        self.img = img
        self.img.set_colorkey((255, 255, 255))
        self.pos = position
        self.old_pos = ""

    # Lets find out if 2 objects are in the same place
    def meet(self, obj):  
        if self.position == obj.position:
            return True
        else:
            return False
            
    @property
    def image(self):
        return self.img

    @property
    def position(self):
        return self.pos
