#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 02:14:43 2018

@author: dsambugaro
"""
import pygame as pg
from pygame.locals import *
from glob import glob

from settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, game, position):
        pg.sprite.Sprite.__init__(self)
        #self.image = load_image('elf_m_idle_anim_f0.png').convert_alpha()
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
        
        self.velocity = PLAYER_VELOCITY
        self._position = vec(position[0], position[1])
        self._old_position = self.position
        self.rect = self.image.get_rect()
        self.feet = pg.Rect(0, 0, self.rect.width * .5, 8)
        
        self.right = False
        self.left = False

    @property
    def position(self):
        return list(self._position)

    @position.setter
    def position(self, value):
        self._position = list(value)
    
    def load_character_animation(self, character, genre, action):
        sprites = glob(HEROES_SPRITES_DIR + '/' + character + '_' + genre +'_' + action + '_anim_f*.png')
        sprites.sort()
        
        for i in range(len(sprites)):
            sprites[i] = pg.image.load(sprites[i]).convert_alpha()
        
        return sprites
    
    def get_keys(self):
        pressed = pg.key.get_pressed()
        
        if pressed[K_UP]  or pressed[K_w]:
            self.velocity.y = -PLAYER_MOVE_SPEED
        elif pressed[K_DOWN]  or pressed[K_s]:
            self.velocity.y = PLAYER_MOVE_SPEED
        else:
            self.velocity.y = 0

        if pressed[K_LEFT] or pressed[K_a]:
            self.velocity.x = -PLAYER_MOVE_SPEED
        elif pressed[K_RIGHT]  or pressed[K_d]:
            self.velocity.x = PLAYER_MOVE_SPEED
        else:
            self.velocity.x = 0
    
    def update_by_time(self, dt):
        if self.velocity.x > 0:
            self.images = self.images_right_run
            self.right = True
            self.left = False
            
        elif self.velocity.x < 0:
            self.images = self.images_left_run
            self.left = True
            self.right = False
            
        elif self.velocity.y > 0 or self.velocity.y < 0:
            if self.left:
                self.images = self.images_left_run
            if self.right:
                self.images = self.images_right_run
                
        elif self.velocity.x == 0 and self.velocity.y == 0:
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
        self.update_by_time(dt)
        self._old_position = self._position
        self._position.x += self.velocity.x * dt
        self._position.y += self.velocity.y * dt
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self, dt):
        self._position = self._old_position
        self.rect.topleft = self._position
        self.feet.midbottom = self.rect.midbottom