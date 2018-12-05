#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:14:43 2018

@author: dsambugaro
"""
import pygame as pg
from pygame.locals import *
from glob import glob

from pygame.math import Vector2
vec = Vector2

from settings import *
import save

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.weapon = WEAPONS['rusty_sword']
        self.game = game
        self.images_idle = self.load_character_animation('elf','m','idle')
        self.images_run = self.load_character_animation('elf','m','run')
        self.images_right_idle = self.images_idle
        self.images_right_run = self.images_run
        self.images_left_idle = [pg.transform.flip(image, True, False) for image in self.images_idle]
        self.images_left_run = [pg.transform.flip(image, True, False) for image in self.images_run]
        self.index = 0
        self.images = self.images_idle
        self.image = self.images[self.index]
        self.image_run = self.images_run[self.index]

        self.animation_time = 0.12
        self.current_time = 0

        self.animation_frames = len(self.images)
        self.current_frame = 0
        
        self._position = [x, y]
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pg.Rect(0, 0, self.rect.width * .55, 6)

        self.right = False
        self.left = False
        
        self.HP = HP
        self.velocity = PLAYER_VELOCITY
        self.speed = PLAYER_MOVE_SPEED
        
        self._steps = 0
        
    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)
    
    @property
    def steps(self):
        return int(self._steps/20)
    
    @steps.setter
    def steps(self, value):
        if value > 0:
            self._steps = value
        else:
            self._steps = 0
    
    def load_save(self):
        self.speed = save.PLAYER_MOVE_SPEED
        self.HP = save.HP
    
    def load_character_animation(self, character, genre, action):
        sprites = glob(HEROES_SPRITES_DIR + '/' + character + '_' + genre +'_' + action + '_anim_f*.png')
        sprites.sort()
        
        for i in range(len(sprites)):
            sprites[i] = pg.image.load(sprites[i]).convert_alpha()
        
        return sprites
    
    def get_keys(self):
        pressed = pg.key.get_pressed()
        if not self.game.dialog:
            if pressed[K_UP]  or pressed[K_w]:
                self._steps += 1
                self.velocity[1] = -self.speed
            elif pressed[K_DOWN]  or pressed[K_s]:
                self._steps += 1
                self.velocity[1] = self.speed
            else:
                self.velocity[1] = 0
    
            if pressed[K_LEFT] or pressed[K_a]:
                self._steps += 1
                self.velocity[0] = -self.speed
            elif pressed[K_RIGHT]  or pressed[K_d]:
                self._steps += 1
                self.velocity[0] = self.speed
            else:
                self.velocity[0] = 0

    
    def update_time_dependent(self, dt):
        if self.velocity[0] > 0:
            self.images = self.images_right_run
            self.right = True
            self.left = False
            
        elif self.velocity[0] < 0:
            self.images = self.images_left_run
            self.left = True
            self.right = False
            
        elif self.velocity[1] > 0 or self.velocity[1] < 0:
            if self.left:
                self.images = self.images_left_run
            if self.right:
                self.images = self.images_right_run
                
        elif self.velocity[0] == 0 and self.velocity[1] == 0:
            if self.left:
                self.images = self.images_left_idle
            if self.right:
                self.images = self.images_right_idle

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        self.get_keys()
        self.update_time_dependent(dt)
        self._old_position = self._position[:]
        self._position[0] += self.velocity[0] * dt
        self._position[1] += self.velocity[1] * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

class Door(pg.sprite.Sprite):
    def __init__(self, x, y, id_door):
        super().__init__()
        self.image = pg.image.load(SCENARIO_SPRITES_DIR + '/doors_leaf_closed.png').convert_alpha()
        self.rect = self.image.get_rect()
        self._position = [x, y]
        self.id = id_door
    
    def update(self, dt):
        self.rect.topleft = self._position

class Pointer(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pg.image.load(UI_SPRITES_DIR + '/arrow.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self._position = [pos[0], pos[1]]
    
    def update(self, dt):
        self.rect.topleft = self._position

class NPC(pg.sprite.Sprite):
    def __init__(self, x, y, npc, action='idle', w=None, h=None):
        super().__init__()
        self.images_idle = self.load_character_animation(npc, action)
        self.index = 0
        self.images = self.images_idle
        if w and h:
            for i in range(len(self.images)):
                self.images[i] = pg.transform.scale(self.images[i], (w, h))
        self.image = self.images[self.index]
        self.animation_time = 0.12
        self.current_time = 0

        self.animation_frames = len(self.images)
        self.current_frame = 0
        if w and h:
            self._position = [x-w/2, y-h/2]
        else:
            self._position = [x, y]
        self.rect = self.image.get_rect()

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)
    
    def load_character_animation(self, npc, action):
        sprites = glob(ENEMIES_SPRITES_DIR  + '/' + npc + '_' + action + '_anim_f*.png')
        sprites.sort()
        
        for i in range(len(sprites)):
            sprites[i] = pg.image.load(sprites[i]).convert_alpha()
        
        return sprites

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.topleft = self._position


class OBJ(pg.sprite.Sprite):
    def __init__(self, x, y, obj):
        super().__init__()
        self.images_idle = self.load_obj_animation(obj)
        self.index = 0
        self.images = self.images_idle
        self.image = self.images[self.index]

        self.animation_time = 0.12
        self.current_time = 0

        self.animation_frames = len(self.images)
        self.current_frame = 0

        self._position = [x, y]
        self.rect = self.image.get_rect()

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)
    
    def load_obj_animation(self, obj):
        sprites = glob(OBJECTS_SPRITES_DIR  + '/' + obj + '_anim_f*.png')
        sprites.sort()
        
        for i in range(len(sprites)):
            sprites[i] = pg.image.load(sprites[i]).convert_alpha()
        
        return sprites

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

    def update(self, dt):
        self.update_time_dependent(dt)
        self.rect.topleft = self._position