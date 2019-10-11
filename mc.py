#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import json
from random import *

class Game:

	GRID = {}
	IMG_SOL = ""
	IMG_MUR = ""
	WIN = False

	def __init__(self, map_file, img_sol, img_mur, img_congratulations, img_dead):

		self.load_grid(map_file)
		self.IMG_SOL = self.load_img(img_sol)
		self.IMG_MUR = self.load_img(img_mur)
		self.img_win = self.load_img(img_congratulations)
		self.img_lost = self.load_img(img_dead)

	@classmethod
	def load_img(cls,img):
		return pygame.image.load(img).convert_alpha()

	@classmethod
	def load_grid(cls,map_file):
		with open(map_file) as f:
			data = json.load(f)
			# load all the data contained in this file. data = entries
			line = 0
			for entry in data:
				for colomn in range (0,15):
					key = str(line)+","+str(colomn)
					cls.GRID[key] = entry["maze"][colomn:colomn+1]
				
					if cls.GRID[key] == "S":
						cls.GRID["mac"] = key

					if cls.GRID[key] == "E":
						cls.GRID["gardian"] = key

				line = line+1

	@property
	def grid(self):
		return(self.GRID)

	def look_for_a_free_slot(self):
		line = randint(0,14)
		colomn = randint(0,14)
		key = str(line)+","+str(colomn)
		while(self.GRID[key]) != " ":
			line = randint(0,14)
			colomn = randint(0,14)
			key = str(line)+","+str(colomn)
		self.GRID[key] = "-"	
		return key

	def display(self,fenetre):
		for line in range(0,15):
			for colomn in range(0,15):
				key = str(line)+","+str(colomn)
				fenetre.blit(self.IMG_SOL, (colomn*32, line*43))

				if self.GRID[key] == "*":
					fenetre.blit(self.IMG_MUR, (colomn*32, line*43))
	
	def meet(self,obj1,obj2): # Lets find out if 2 objects are in the same place
		end = False
		if obj1.position == obj2.position:
			end = True
		else:
			end = False

		if obj1.nb_tools == 3: # If Obj1 has 3 tools then we consider that it has won against Obj2
			self.WIN = True
		
		return end


	def show_end_msg(self,fenetre): # Display a result message at the end of a game
		if self.WIN:
			fenetre.blit(self.img_win, (10, 10))
		else:
			fenetre.blit(self.img_lost, (10, 10))

		
class Object:

	def __init__(self, img, position):
		self.img = pygame.image.load(img).convert_alpha()
		self.img.set_colorkey((255,255,255))
		self.pos = position
		self.nb_tools = 0
		self.old_pos = ""

	def move(self,grid,hor,vert): # Move an object
		new_pos = str(int(self.pos.split(",")[0])+vert)+","+str(int(self.pos.split(",")[1])+hor)
		if self.in_the_grid(new_pos):
			if grid[new_pos] != "*":
				self.old_pos = self.pos
				self.pos = new_pos 

	def Collect_tools(self,grid): # Collect an object (to call right after a move)
		if grid[self.pos] == "-":
			self.nb_tools += 1 
			grid[self.pos] == " "
			return True
		return False

	@classmethod
	def in_the_grid(cls,position): # check if an object is on the grid of the game
		i = int(position.split(",")[0])
		j = int(position.split(",")[1]) 
		if i<0 or i>14 or j<0 or j>14:
			return False
		return True

	def display(self,fenetre,grid): # reset old position and diplay new position object
		if self.old_pos!="":
			fenetre.blit(grid.IMG_SOL, (int(self.old_pos.split(",")[1])*32, int(self.old_pos.split(",")[0])*43))
		fenetre.blit(self.image, (int(self.pos.split(",")[1])*32, int(self.pos.split(",")[0])*43))

	@property
	def image(self):
		return self.img

	@property
	def position(self):
		return self.pos

def main():
	pygame.init()
	myClock = pygame.time.Clock()
	fenetre = pygame.display.set_mode((480,645), RESIZABLE)

	# We create the objects, load their images and their starting position
	game = Game("maze.json","ressource/sol.png","ressource/mur.png","ressource/congratulations.png","ressource/dead.png")
	gyver = Object("ressource/MacGyver.png", game.grid["mac"])
	gardian = Object("ressource/Gardien.png", game.grid["gardian"])
	t1 = Object("ressource/seringue.png", game.look_for_a_free_slot())
	t2 = Object("ressource/tube_plastique.png", game.look_for_a_free_slot())
	t3 = Object("ressource/ether.png", game.look_for_a_free_slot())

	# We display the objects of the game
	game.display(fenetre)
	gyver.display(fenetre,game)
	gardian.display(fenetre,game)
	t1.display(fenetre,game)
	t2.display(fenetre,game)
	t3.display(fenetre,game.GRID)
	pygame.display.flip()

	end_game = False
	while not end_game:
		# Loop on all events managed by Pygame
		for event in pygame.event.get():        
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE or game.meet(gyver,gardian):
				# The window has been closed or The ESC key has been pressed.
				pygame.time.delay(3000) # wait 3 seconds before going out to display the WIN or LOST message
				end_game = True # Indicates to exit the loop.
	            
			if event.type == KEYDOWN: 
				# Change the coordinates of the position of the character
				if event.key == K_RIGHT: 
					gyver.move(game.GRID,1,0)
					gyver.Collect_tools(game.GRID)

				elif event.key == K_LEFT: 
					gyver.move(game.GRID,-1,0)
					gyver.Collect_tools(game.GRID)

				elif event.key == K_UP: 
					gyver.move(game.GRID,0,-1)
					gyver.Collect_tools(game.GRID)

				elif event.key == K_DOWN: 
					gyver.move(game.GRID,0,1)
					gyver.Collect_tools(game.GRID)
				
				gyver.display(fenetre,game)

				if game.meet(gyver,gardian):
					game.show_end_msg(fenetre)
					pygame.display.update()

				myClock.tick(60)
				pygame.display.flip()
	
	pygame.display.quit() # close the window
	pygame.quit() # quit pygame and the game 

main()
