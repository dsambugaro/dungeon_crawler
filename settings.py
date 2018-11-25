#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:20:07 2018

@author: dsambugaro
"""
from pygame.math import Vector2
vec = Vector2

MAPS_DIR = 'maps'
HEROES_SPRITES_DIR = 'art/heroine'

TEMPLE = 'temple.tmx'

# Game settings
WINDOW_RESOLUTION = (1280, 720)

# Player settings
PLAYER_VELOCITY = vec(0, 0)
PLAYER_MOVE_SPEED = 150