#! /usr/bin/env python3
# coding: utf-8

import pygame

pygame.init()
WINDOW = pygame.display.set_mode((480, 675))

WALL = pygame.image.load('ressource/mur.png').convert_alpha()
GROUND = pygame.image.load('ressource/sol.png').convert_alpha()
MAC = pygame.image.load('ressource/MacGyver.png').convert_alpha()
GARDIAN = pygame.image.load('ressource/Gardien.png').convert_alpha()
OBJ1 = pygame.image.load('ressource/seringue.png').convert_alpha()
OBJ2 = pygame.image.load('ressource/tube_plastique.png').convert_alpha()
OBJ3 = pygame.image.load('ressource/ether.png').convert_alpha()

FONT = pygame.font.Font('ressource/stocky.ttf', 25)
FONT_COLOR = (255, 255, 255)
FONT_END_MSG = pygame.font.Font('ressource/winter.ttf', 45)
FONT_END_MSG_COLOR = (255, 255, 255)
FONT_TOOLS = pygame.font.Font('ressource/square.ttf', 15)