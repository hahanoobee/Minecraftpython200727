# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:58:18 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print(mc.player.getTilePos())