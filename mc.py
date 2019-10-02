#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import json
from random import *

class Map():
	def __init__(self):
		global my_map, fenetre, img_sol, img_mur, img_mac, img_gardian, img_t1, img_t2, img_t3 
		# Permet de rendre la fenêtre de taille ajustable.
		fenetre = pygame.display.set_mode((480,645), RESIZABLE)
		# On charge les images
		img_sol = pygame.image.load("ressource/sol.png").convert_alpha()
		img_mur = pygame.image.load("ressource/mur.png").convert_alpha()

		img_mac = pygame.image.load("ressource/MacGyver.png").convert_alpha()
		img_gardian = pygame.image.load("ressource/Gardien.png").convert_alpha()
		img_t1 = pygame.image.load("ressource/seringue.png").convert_alpha()
		img_t2 = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
		img_t3 = pygame.image.load("ressource/ether.png").convert_alpha()

		img_t1.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
		img_t2.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
		img_t3.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent

		# Init de la carte
		my_map = {}
		my_map["nb_tools"] = 0

	def load_maze(self):
		with open("maze.json") as f:
			data = json.load(f)
			# load all the data contained in this file. data = entries
			line = 0
			for entry in data:
				for colomn in range (0,15):
					key = str(line)+","+str(colomn)
					my_map[key] = entry["maze"][colomn:colomn+1]
				
					if my_map[key] == "S":
						my_map["mac"] = key

					if my_map[key] == "E":
						my_map["gardian"] = key

				line = line+1

	def display(self):
		for line in range(0,15):
			for colomn in range(0,15):
				key = str(line)+","+str(colomn)
				fenetre.blit(img_sol, (colomn*32, line*43))

				if my_map[key] == "*":
					fenetre.blit(img_mur, (colomn*32, line*43))

				if my_map["1"] == key:
					fenetre.blit(img_t1, (colomn*32, line*43))
		
				if my_map["2"] == key:
					fenetre.blit(img_t2, (colomn*32, line*43))

				if my_map["3"] == key:
					fenetre.blit(img_t3, (colomn*32, line*43))

				if my_map[key] == "E":
					fenetre.blit(img_gardian, (colomn*32, line*43))

				if my_map["mac"] == key:
					fenetre.blit(img_mac, (colomn*32, line*43))

class Character():

	def move(self,hor,vert):
		actualLine = my_map["mac"].split(",")[0]
		actualcolomn = my_map["mac"].split(",")[1]
		newline = int(actualLine) + int(vert)
		newcolomn = int(actualcolomn) + int(hor)
		newKey = str(newline)+","+str(newcolomn)

		if not((newline<0) or (newline>14) or (newcolomn<0) or 
			(newcolomn>14) or (my_map[newKey]=="*")):
			my_map[my_map["mac"]] = " "
			#if my_map["mac"] == my_map["S"]:
			#	my_map[my_map["mac"]] = "S"
			if my_map["mac"] == my_map["gardian"]:
				my_map[my_map["mac"]] = "E"
				
			my_map["mac"] = newKey	

	def catch_tool(self):
		for i in range(1,4):
			if my_map["mac"] == my_map[str(i)]:
				my_map[str(i)] = " "
				my_map["nb_tools"] = int(my_map["nb_tools"]) + 1
				print(my_map["nb_tools"])

	def kill_gardian(self):
		if my_map["mac"] == my_map["gardian"]:
			if my_map["nb_tools"] == 3:
				print("You win !!")
				return False
			else:
				print("You are dead")
				return False
		return True

class Tools():
	image = ""

	def __init__(self,tool_number,img):
		x = randint(0,14)
		y = randint(0,14)
		key = str(x)+","+str(y)
		while(my_map[key]) != " ":
			x = randint(0,14)
			y = randint(0,14)
			key = str(x)+","+str(y)
		my_map[str(tool_number)] = key
		my_map[key] = str(tool_number)
		image = pygame.image.load(img).convert_alpha()
		print(str(tool_number)+" "+key)

# Initialisation des modules de Pygame
pygame.init()
myClock = pygame.time.Clock()

map = Map()
map.load_maze()

mac = Character()
guardian = Character()
t1 = Tools(1,"ressource/seringue.png")
t2 = Tools(2,"ressource/tube_plastique.png")
t3 = Tools(3,"ressource/ether.png")

map.display()
pygame.display.flip()

continuer = True
while continuer:
	# Boucle sur tous les événements gérés par Pygame
	for event in pygame.event.get():        
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			# La fenêtre a été fermée ou La touche ESC a été pressée.
			continuer = False # Indique de sortir de la boucle.
            
		if event.type == KEYDOWN:  # KEYUP existe aussi
			# Change les coordonnées de la position de la personne
			if event.key == K_RIGHT: 
				mac.move(1,0)
				mac.catch_tool()
				continuer = mac.kill_gardian()
			if event.key == K_LEFT: 
				mac.move(-1,0)
				mac.catch_tool()
				continuer = mac.kill_gardian()
			if event.key == K_UP: 
				mac.move(0,-1)
				mac.catch_tool()
				continuer = mac.kill_gardian()
			if event.key == K_DOWN: 
				mac.move(0,1)
				mac.catch_tool()
				continuer = mac.kill_gardian()

			map.display()
			pygame.display.flip()

	# Pour avoir un autorepeat si une touche est pressée.
	pygame.key.set_repeat(10, 3) # répétition de la touche toutes les ... [ms]
		
	myClock.tick(60)

pygame.display.quit() # ferme la fenêtre, c.f. https://www.pygame.org/docs/ref/display.html
pygame.quit() # quitte pygame, c.f. https://www.pygame.org/docs/ref/pygame.htmlv