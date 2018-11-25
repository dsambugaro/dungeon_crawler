#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 16:04:21 2018

@author: dsambugaro
"""

import sys
import os.path

import pygame as pg
import pyscroll
import pyscroll.data
from pygame.locals import *
from pytmx.util_pygame import load_pygame
from pyscroll.group import PyscrollGroup

from settings import *
from sprites import Player
from tilemap import Map


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
        self.player = Player(self, (160,718))
        self.new_map(TEMPLE)
        self.new_group()

    def new_map(self, filename):
        self.map = Map(get_map(filename), self.screen)
        self.walls = self.map.getWalls()

    def new_group(self):
        self.group = self.map.group()
        self.group.add(self.player)

    def quit_game(self):
        pg.quit()
        sys.exit()

    def draw(self):

        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)

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
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back(dt)

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
