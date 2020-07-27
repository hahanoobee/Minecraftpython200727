# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:08:23 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=-240.5
y=80.5
z=230.5


mc.player.setPos(x,y,z)