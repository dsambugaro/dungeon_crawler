#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:04:21 2018

@author: dsambugaro
"""

import sys
import os.path

import pygame as pg
from pygame.locals import *
from pyscroll.group import PyscrollGroup

from settings import *
from tilemap import Map
from sprites import Player, Door

def init_screen(width, height):
    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
    return screen

def get_map(filename):
    return os.path.join(MAPS_DIR, filename)

class MainGame:
    def __init__(self):
        pg.init()
        pg.display.set_caption('< a nice name here >')
        self.running = False
        self.screen = pg.display.set_mode(WINDOW_RESOLUTION)
        self.new_map(TEMPLE)
        
        self.group = PyscrollGroup(map_layer=self.map.layer, default_layer=2)
        
        self.all = []
        self.obstacle = []
        self.doors = []
        print(self.map.map_data)
        for object in self.map.map_data.tmx.objects:
            if object.name == 'wall' and object.visible:
                self.all.append(pg.Rect(object.x, object.y, object.width, object.height))
                self.obstacle.append(pg.Rect(object.x, object.y, object.width, object.height))
            if object.name == 'door' and object.visible:
                self.all.append(pg.Rect(object.x, object.y, object.width, object.height))
                self.obstacle.append(pg.Rect(object.x, object.y, object.width, object.height))
                self.doors.append(Door(object.x,object.y))
            if object.name == 'init' and object.visible:
                self.all.append(pg.Rect(object.x, object.y, object.width, object.height))
                self.player = Player(self, object.x,object.y)
        self.player = Player(self, 160,160)
        self.group.add(self.player)

    def new_map(self, filename):
        self.map = Map(get_map(filename), self.screen)

    def quit_game(self):
        pg.quit()
        sys.exit()

    def update_obstacles(self):
        self.obstacle = []
        for object in self.map.tmx_data.objects:
            if object.name == 'wall' or object.name == 'door' and object.visible:
                self.obstacle.append(pg.Rect(object.x, object.y, object.width, object.height))

    def draw_hp(self):
        full = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_full.png')).convert_alpha()
        half = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_half.png')).convert_alpha()
        empty = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_empty.png')).convert_alpha()
        
        full = pg.transform.scale(full, (HP_SIZE, HP_SIZE))
        half = pg.transform.scale(half, (HP_SIZE, HP_SIZE))
        half = pg.transform.flip(half, True, False)
        empty = pg.transform.scale(empty, (HP_SIZE, HP_SIZE))
        
        hearts_full = int((self.player.HP / 0.2)/10)
        hearts = [full for i in range(hearts_full)]
        
        if self.player.HP % 2 != 0:
            hearts.append(half)

        for i in range(HEARTS-hearts_full):
            hearts.append(empty)
        
        for i in range(0, HEARTS):
                self.screen.blit(hearts[i], (WINDOW_RESOLUTION[0] - HP_SIZE*(i+1), 10))
        
        pg.display.update()


    def draw(self):
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.draw_hp()

#        for sprite in self.group.sprites():
#            pg.draw.rect(self.screen, (255, 255, 255), sprite.feet)
#        
#        for wall in self.obstacle:
#            pg.draw.rect(self.screen, (255, 255, 255), wall)

    def handle_input(self):
        poll = pg.event.poll

        event = poll()
        while event:
            if event.type == QUIT:
                self.running = False
                self.quit_game()
                break

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    self.quit_game()
                    break

                elif event.key == K_EQUALS:
                    self.map.zoomIn(.25)

                elif event.key == K_MINUS:
                    self.map.zoomOut(.25)

            elif event.type == VIDEORESIZE:
                init_screen(event.w, event.h)
                self.map_layer.set_size((event.w, event.h))

            event = poll()

    def update(self, dt):
        self.group.update(dt)
        
        if self.player.feet.collidelist(self.obstacle) > -1:
            self.player.move_back(dt)

    def run(self):
        clock = pg.time.Clock()
        self.running = True

        from collections import deque
        times = deque(maxlen=30)

        try:
            while self.running:
                dt = clock.tick() / 1000.
                times.append(clock.get_fps())

                self.handle_input()
                self.update(dt)
                self.draw()
                pg.display.flip()

        except KeyboardInterrupt:
            self.running = False
            self.quit_game()
            


if __name__ == "__main__":
    
    try:
        game = MainGame()
        game.run()
    except:
        pg.quit()
        raise
