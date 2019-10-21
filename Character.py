import pygame
from pygame.locals import *
from Object import *

# Class in charge to manage objects as MacGyver, gardian, tools
class Character(Object):

    def __init__(self, img, position):
        super().__init__(img, position)
        self.nb_tools = 0

    def move_object(self, map):
        for event in pygame.event.get():        
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                # The window has been closed or The ESC key has been pressed.
                return False  # Indicates to exit the loop.

            if event.type == KEYDOWN: 
                # Change the coordinates of the position of the character
                if event.key == K_RIGHT: 
                    self.move(map.grid, 1, 0)

                elif event.key == K_LEFT: 
                    self.move(map.grid, -1, 0)

                elif event.key == K_UP: 
                    self.move(map.grid, 0, -1)

                elif event.key == K_DOWN: 
                    self.move(map.grid, 0, 1)

                self.collect_tools(map.grid)

        return True

    def move(cls, grid, hor, vert):  # Move an object
        new_pos = str(int(cls.pos.split(",")[0]) + vert) + "," + \
                    str(int(cls.pos.split(",")[1])+hor)
        if cls.in_the_grid(new_pos):
            if grid[new_pos] != "*":
                cls.old_pos = cls.pos
                cls.pos = new_pos 

    def collect_tools(cls, grid):  # Collect an object (to call right after a move)
        if grid[cls.pos] == "-":
            cls.nb_tools += 1 
            grid[cls.pos] = " "

    @classmethod
    def in_the_grid(cls, position):  # check if an object is on the grid of the game
        i = int(position.split(",")[0])
        j = int(position.split(",")[1]) 
        if i < 0 or i > 14 or j < 0 or j > 14:
            return False
        return True

    @property
    def image(self):
        return self.img

    @property
    def position(self):
        return self.pos
