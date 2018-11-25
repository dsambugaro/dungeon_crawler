#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 03:09:21 2018

@author: dsambugaro
"""

import pygame as pg
import pyscroll
from pyscroll.group import PyscrollGroup
from pytmx.util_pygame import load_pygame

class Map:
    def __init__(self, filename, screen, zoom=4):
        self.zoom = zoom
        self.filename = filename
        self.screen = screen
        self.tmx_data = load_pygame(self.filename)
        
        self.walls = []
        for object in self.tmx_data.objects:
            self.walls.append(pg.Rect(
                object.x, object.y,
                object.width, object.height))
        
        self.camera_init()
            
    def camera_init(self):
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size(), clamp_camera=False, tall_sprites=1)
        self.map_layer.zoom = self.zoom
    
    def group(self):
        return PyscrollGroup(map_layer=self.map_layer, default_layer=2)
    
    def zoom():
        return self.map_layer.zoom
    
    def zoomIn(self, value):
        self.map_layer.zoom += value
    
    def zoomOut(self, value):
        new_zoom = self.map_layer.zoom - value
        if new_zoom > 0:
            self.map_layer.zoom = new_zoom
    
    def getWalls(self):
        return self.walls