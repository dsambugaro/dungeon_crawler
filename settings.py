#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:20:07 2018

@author: dsambugaro
"""

MAPS_DIR = 'maps'
HEROES_SPRITES_DIR = 'art/heroine'
ENEMIES_SPRITES_DIR = 'art/enemies'
OBJECTS_SPRITES_DIR = 'art/objects'

SCENARIO_SPRITES_DIR = 'art/scenario'
UI_SPRITES_DIR = 'art/interface'

TEMPLE = 'temple.tmx'

HAS_SAVE = False

# UI settings
HP_SIZE = 50
HEARTS = 5

# Weapons settings
WEAPONS = {}

WEAPONS['rusty_sword'] = {
        'damage': 1,
        'critical':0.1,
        'sprite': 'weapon_rusty_sword.png'
        }

WEAPONS['regular_sword'] = {
        'damage': 3,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

WEAPONS['regular_sword'] = {
        'damage': 3,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

# Enemies
ENEMIES = {}

ENEMIES[''] = {
        'damage': 3,
        'hp': 10,
        'critical':0.2,
        'sprite': 'weapon_regular_sword.png'
        }

# Dialogs
DIALOGS = {}

DIALOGS['test'] = [
        [
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS'
        ],
        [
                '!@#$%*() ã àá ç õ',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS'
        ]
    ]

DIALOGS['first'] = [
        [
                'Lorem asasdasdasdasdasdasasd asdasdasdasdasdasdasdasdsd',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS'
        ],
        [
                '!@#$%*() ã àá ç õ',
                'ASDASDASDASDASDASDASDASDAS DASDASDASDASDASSDSDS'
        ]
    ]

# Game settings
WINDOW_RESOLUTION = (1280, 720)

# Player settings
PLAYER_VELOCITY = [0, 0]
PLAYER_MOVE_SPEED = 150
HP = 10
INVENTARY = {}
INVENTARY['weapons'] = []
INVENTARY['shields'] = []