#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 03:09:21 2018

@author: dsambugaro
"""

import pyscroll
from pytmx.util_pygame import load_pygame

class Map:
    def __init__(self, filename, screen, zoom=4):
        self.zoom = zoom
        self.filename = filename
        self.screen = screen
        self.tmx_data = load_pygame(self.filename)

        self.camera_init()


    def camera_init(self):
        self.map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size(), clamp_camera=False, tall_sprites=1)
        self.layer.zoom = self.zoom

    def zoom(self):
        return self.layer.zoom

    def zoomIn(self, value):
        self.layer.zoom += value

    def zoomOut(self, value):
        new_zoom = self.layer.zoom - value
        if new_zoom > 0:
            self.layer.zoom = new_zoom