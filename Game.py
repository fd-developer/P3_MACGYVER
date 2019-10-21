#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
from constants import *
from Map import *
from Displaymap import *
from Object import *
from Character import *

# Class in charge of controlling the roll of the game
class Game:

    def __init__(self):
        self.WIN = 2

    # Starting the game
    def start(self):
        pygame.init()
        map = Map()
        screen = DisplayMap()
        mac = Character(MAC, map.grid["mac"])
        gardian = Character(GARDIAN, map.grid["gardian"])
        t1 = Object(OBJ1, map.search_a_free_slot())
        t2 = Object(OBJ2, map.search_a_free_slot())
        t3 = Object(OBJ3, map.search_a_free_slot())

        screen.display_global(map, mac, gardian, t1, t2, t3)

        play = True
        while play:
            play = mac.move_object(map)
            screen.display_object(mac)
            screen.display_nb_tools(mac)
            if mac.meet(gardian):
                self.WIN = (mac.nb_tools == 3)
                play = False

        screen.show_end_msg(self.WIN)
        self.WIN = 2
        return screen.wait()

    def __del__(self):
        pygame.display.quit()  # close the window
        pygame.quit()  # quit pygameÒ
