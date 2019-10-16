#! /usr/bin/env python3
# coding: utf-8

import pygame

pygame.init()
WINDOW = pygame.display.set_mode((480, 645))

WALL = pygame.image.load('ressource/mur.png').convert_alpha()
GROUND = pygame.image.load('ressource/sol.png').convert_alpha()
MAC = pygame.image.load('ressource/MacGyver.png').convert_alpha()
GARDIAN = pygame.image.load('ressource/Gardien.png').convert_alpha()
OBJ1 = pygame.image.load('ressource/seringue.png').convert_alpha()
OBJ2 = pygame.image.load('ressource/tube_plastique.png').convert_alpha()
OBJ3 = pygame.image.load('ressource/ether.png').convert_alpha()
WIN = pygame.image.load('ressource/congratulations.png').convert_alpha()
LOST = pygame.image.load('ressource/dead.png').convert_alpha()
