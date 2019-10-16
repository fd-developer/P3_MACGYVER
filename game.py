#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
from constants import *
from map import *
from displaymap import *
from object import *


# Class in charge of controlling the roll of the game
class Game:

	def __init__(self):
		self.WIN = 2

	# Lets find out if 2 objects are in the same place
	def meet(self, obj1, obj2):  
		if obj1.position == obj2.position:
			return True
		else:
			return False

	# Starting the game
	def start(self):
		pygame.init()
		map = Map()
		screen = DisplayMap()
		mac = Object(MAC, map.grid["mac"])
		gardian = Object(GARDIAN, map.grid["gardian"])
		t1 = Object(OBJ1, map.search_a_free_slot())
		t2 = Object(OBJ2, map.search_a_free_slot())
		t3 = Object(OBJ3, map.search_a_free_slot())

		screen.display_global(map, mac, gardian, t1, t2, t3)

		play = True
		while play:
			play = mac.move_object(map)
			screen.display_object(mac)
			if self.meet(mac, gardian):
				self.WIN = (mac.nb_tools == 3)
				play = False

		screen.show_end_msg(self.WIN)
		screen.wait()

	def __del__(self):
		pygame.display.quit()  # close the window
		pygame.quit()  # quit pygame