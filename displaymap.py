import pygame
from pygame.locals import *
from constants import *


# Class grouping all methods and variables related to pygame
class DisplayMap:

	# View map and all objects
	def display_global(self, map, o1, o2, o3, o4, o5):
		self.title = pygame.display.set_caption('Aidez MacGyver')
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

	def display_nb_tools(cls, object): 
		pygame.draw.rect(WINDOW, (0, 0, 0), (0,660,200,665))
		COLOR = (255, 0, 0)
		if object.nb_tools == 3:
			COLOR = (0, 255, 0)
		msg = FONT_TOOLS.render('Tools : '+str(object.nb_tools), True, COLOR)
		WINDOW.blit(msg, (0, 660))
		pygame.display.flip()

	# View map and all objects
	def show_end_msg(self, win): 
		if win == 1:
			msg = FONT_END_MSG.render('Congratulations !!', True, FONT_END_MSG_COLOR)
			WINDOW.blit(msg, (60, 300))
		elif win == 0:
			msg = FONT_END_MSG.render('You are dead !!', True, FONT_END_MSG_COLOR)
			WINDOW.blit(msg, (100, 300))
		pygame.display.flip()

	# Wait for an action from player
	def wait(self):
		msg = FONT.render('R to Replay', True, FONT_COLOR)
		WINDOW.blit(msg, (170, 360))
		msg = FONT.render('or another key to quit', True, FONT_COLOR)
		WINDOW.blit(msg, (110, 380))
		pygame.display.flip()

		wait = True
		while wait:
			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN:
					wait = False
					if event.key == 114:
						return True
					else:
						return False