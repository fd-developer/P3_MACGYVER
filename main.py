#! /usr/bin/env python3
# coding: utf-8

# Run this file to start the game
from Game import *

game = Game()
play = True
while play:
    play = game.start()
