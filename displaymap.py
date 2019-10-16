import pygame
from pygame.locals import *
from constants import *


# Class grouping all methods and variables related to pygame
class DisplayMap:

	# View map and all objects
	def display_global(self, map, o1, o2, o3, o4, o5):
		self.display_map(map)
		self.display_object(o1)
		self.display_object(o2)
		self.display_object(o3)
		self.display_object(o4)
		self.display_object(o5)

	# View map WALL end GROUND
	@classmethod
	def display_map(cls, map):

			for line in range(0, 15):
				for colomn in range(0, 15):
					key = str(line)+","+str(colomn)
					WINDOW.blit(GROUND, (colomn*32, line*43))
					if map.grid[key] == "*":
						WINDOW.blit(WALL, (colomn*32, line*43))
			pygame.display.flip()

	# Reset old position and diplay new object position
	@classmethod
	def display_object(cls, object): 
		if object.old_pos != "":
			WINDOW.blit(GROUND, (int(object.old_pos.split(",")[1])*32, \
						int(object.old_pos.split(",")[0])*43))
		
		WINDOW.blit(object.image, (int(object.pos.split(",")[1])*32, \
					int(object.pos.split(",")[0])*43))

		pygame.display.flip()

	# View map and all objects
	def show_end_msg(self, win): 
		if win == 1:
			WINDOW.blit(WIN, (100, 300))
		elif win == 0:
			WINDOW.blit(LOST, (100, 300))
		pygame.display.flip()

	# Wait for an action from player
	def wait(self):
		wait = True
		while wait:
			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN:
					wait = False