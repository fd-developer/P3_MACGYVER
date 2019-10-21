#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import json
from random import *


# Class in charge to manage the map
class Map:

    GRID = {}

    def __init__(self):
        self.load_grid("maze.json")

    @classmethod
    def load_grid(cls, map_file):
        with open(map_file) as f:
            data = json.load(f)
            # load all the data contained in this file. data = entries
            line = 0
            for entry in data:
                for colomn in range(0, 15):
                    key = str(line)+","+str(colomn)
                    cls.GRID[key] = entry["maze"][colomn:colomn+1]
                
                    if cls.GRID[key] == "S":
                        cls.GRID["mac"] = key

                    if cls.GRID[key] == "E":
                        cls.GRID["gardian"] = key

                line = line + 1

    @property
    def grid(self):
        return(self.GRID)

    def search_a_free_slot(self):
        line = randint(0, 14)
        colomn = randint(0, 14)
        key = str(line)+","+str(colomn)
        while(self.GRID[key]) != " ":
            line = randint(0, 14)
            colomn = randint(0, 14)
            key = str(line) + "," + str(colomn)
        self.GRID[key] = "-"    
        return key

