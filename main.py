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
from sprites import Player, Door, NPC

scene = None

def init_screen(width, height):
    screen = pg.display.set_mode((width, height), pg.RESIZABLE)
    return screen

def get_map(filename):
    return os.path.join(MAPS_DIR, filename)

class MainGame:

    def __init__(self):
        pg.init()
        pg.display.set_caption('< a nice name here >')
        self.screen = pg.display.set_mode(WINDOW_RESOLUTION)
        self.openDoors = ['1']
        self.defeated = []
        self.dialog = None
        self.dialog_index = 0
        self.new_map(TEMPLE)

    def new_map(self, filename):
        self.map = Map(get_map(filename), self.screen)
        self.group = PyscrollGroup(map_layer=self.map.layer, default_layer=1)
        self.update_obstacles()

    def update_obstacles(self):
        self.obstacle = []
        self.doors = []
        self.npcs = []
        self.dialogos = []
        self.dialogos_col = []
        for object in self.map.tmx_data.objects:
            if object.name == 'wall' and object.visible:
                self.obstacle.append(pg.Rect(object.x, object.y, object.width, object.height))
            if object.name == 'door' and object.visible and object.type not in self.openDoors:
                door = Door(object.x, object.y, object.type)
                self.doors.append(door.rect)
                self.group.add(door)
            if object.name == 'init' and object.visible:
                rect = pg.Rect(object.x, object.y, object.width, object.height)
                self.player = Player(self, rect.centerx,rect.centery)
                self.group.add(self.player)
            if object.name == 'demon' and object.visible and object.type not in self.defeated:
                self.demon = NPC(object.x,object.y, 'big_demon')
                self.obstacle.append(self.demon.rect)
                self.group.add(self.demon)
#            if object.name == 'orc' and object.visible and object.type not in self.defeated:
#                self.demon = NPC(object.x,object.y, 'ogre')
#                self.obstacle.append(self.demon.rect)
#                self.group.add(self.demon)
#            if object.name == 'zombie' and object.visible and object.type not in self.defeated:
#                self.demon = NPC(object.x,object.y, 'big_zombie')
#                self.obstacle.append(self.demon.rect)
#                self.group.add(self.demon)
            if object.name == 'items' and object.visible:
                self.npc = NPC(object.x,object.y, 'necromancer')
                self.npcs.append(self.npc.rect)
                self.group.add(self.npc)
            if object.name == 'dialogo' and object.visible:
                self.dialogos_col.append(pg.Rect(object.x, object.y, object.width, object.height))
                self.dialogos.append(object)

    def draw_ui(self):

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



    def draw(self):
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen)
        self.draw_ui()

        pg.font.init()
        font_1 = pg.font.SysFont('Source Code Pro Black', 48)

        if self.dialog:
#            this_sentence = []
            if len(DIALOGS[self.dialog]) > self.dialog_index:
                text_box = pg.image.load(os.path.join(UI_SPRITES_DIR, 'text_box.png')).convert_alpha()
                self.screen.blit(text_box, (0,0))
                for i in range(len(DIALOGS[self.dialog][self.dialog_index])):
                    this_sentence = (font_1.render(DIALOGS[self.dialog][self.dialog_index][i],True,(255,255,255)))
                    self.screen.blit(this_sentence,(100,500+((i)*40)))
            else:
                self.dialog_index = 0
                self.dialog = None
        pg.display.update()

#        for sprite in self.group.sprites():
#            pg.draw.rect(self.screen, (255, 255, 255), sprite.rect)
#
#        for wall in self.obstacle:
#            pg.draw.rect(self.screen, (255, 255, 255), wall)

    def handle_input(self, event):
        poll = pg.event.poll

#        event = poll()
        while event:
            if event.key == K_EQUALS:
                self.map.zoomIn(.25)
            elif event.key == K_MINUS:
                self.map.zoomOut(.25)
            elif event.type == VIDEORESIZE:
                self.screen = init_screen(event.w, event.h)
                self.map_layer.set_size((event.w, event.h))
            event = poll()

    def update(self, dt):
        global scene
        self.group.update(dt)

        if self.player.feet.collidelist(self.obstacle) > -1:
            self.player.move_back(dt)
        if self.player.feet.collidelist(self.doors) > -1:
            self.player.move_back(dt)
        if self.player.feet.collidelist(self.npcs) > -1:
            self.player.move_back(dt)
        if self.player.feet.collidelist(self.dialogos_col) > -1:
            if self.dialogos[self.player.feet.collidelist(self.dialogos_col)].texto == 'unread':
                self.dialogos[self.player.feet.collidelist(self.dialogos_col)].texto = 'read'
                self.dialog = self.dialogos[self.player.feet.collidelist(self.dialogos_col)].type
                self.player.velocity = [0,0]

        if self.player.steps >= 10:
            self.player.steps = 0
            scene = scenes['Battle']

class Battle:
    def __init__(self, enemie):
        pg.init()
        pg.display.set_caption('The Guardian')
        self.screen = pg.display.set_mode(WINDOW_RESOLUTION)
        self.dialog = None
        self.dialog_index = 0
        self.new_map('battle.tmx')

    def new_map(self, filename):
        self.map = Map(get_map(filename), self.screen, zoom=1)
        self.group = PyscrollGroup(map_layer=self.map.layer, default_layer=1)
        self.update_obstacles()

    def update_obstacles(self):
        self.acao = []
        self.npcs = []
        self.dialogos = []
        self.dialogos_col = []
        for object in self.map.tmx_data.objects:
            if object.name == 'acao' and object.visible:
                self.acao.append(pg.Rect(object.x, object.y, object.width, object.height))
            if object.name == 'enemie' and object.visible:
                npc = pg.Rect(object.x, object.y, object.width, object.height)
                self.demon = NPC(npc.centerx, npc.centery, 'big_demon')
                self.group.add(self.demon)

    def draw_ui(self):
        full = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_full.png')).convert_alpha()
        half = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_half.png')).convert_alpha()
        empty = pg.image.load(os.path.join(UI_SPRITES_DIR, 'ui_heart_empty.png')).convert_alpha()

        full = pg.transform.scale(full, (HP_SIZE, HP_SIZE))
        half = pg.transform.scale(half, (HP_SIZE, HP_SIZE))
        half = pg.transform.flip(half, True, False)
        empty = pg.transform.scale(empty, (HP_SIZE, HP_SIZE))

        hearts_full = int((scenes['Game'].player.HP / 0.2)/10)
        hearts = [full for i in range(hearts_full)]

        if scenes['Game'].player.HP % 2 != 0:
            hearts.append(half)

        for i in range(HEARTS-hearts_full):
            hearts.append(empty)

        for i in range(0, HEARTS):
                self.screen.blit(hearts[i], (WINDOW_RESOLUTION[0] - HP_SIZE*(i+1), 10))

        pg.display.update()


    def draw(self):
        self.screen.fill((255,255,255))
#        self.group.center(self.demon.rect.center)
        self.group.draw(self.screen)
        self.draw_ui()

    def handle_input(self, event):
        poll = pg.event.poll

#        event = poll()
        while event:
            if event.type == KEYDOWN:
                if event.key == K_h:
                    print('help')
            event = poll()

    def update(self, dt):
        self.group.update(dt)



scenes = {
        'Game': MainGame(),
        'Battle': Battle('k')
          }

scene = scenes['Game']

if __name__ == "__main__":

    try:
        clock = pg.time.Clock()
        running = True

        from collections import deque
        times = deque(maxlen=30)

        running = True
        g = 0
        try:
            while running:
                dt = clock.tick() / 1000.
                times.append(clock.get_fps())
                poll = pg.event.poll
                event = poll()
                while event:
                    if event.type == QUIT:
                        running = False
                        pg.quit()
                        sys.exit()
                        break

                    elif event.type == KEYDOWN:
                        if scene.dialog:
                            if event.key == K_LEFT or event.key == K_RIGHT:
                                scene.dialog_index += 1
                        if event.key == K_ESCAPE:
                            running = False
                            pg.quit()
                            sys.exit()
                            break
#                            scene.new_map('cave.tmx')
                        scene.handle_input(event)
                    event = poll()
                scene.update(dt)
                scene.draw()
                pg.display.flip()

        except KeyboardInterrupt:
            running = False
            pg.quit()
            sys.exit()
    except:
        pg.quit()
        raise
