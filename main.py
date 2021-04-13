import pygame as pyg
import random
import time
import sys

class mzElm():
    up = False # up
    dwn = False # down
    rt = False # right
    lt = False # left

mzSize = [0, 0]
mzSize[0] = 100
mzSize[1] = 100

monRes = [1920, 1080]
border = [0, 0]
size = [monRes[0]-border[0], monRes[1]-border[1]]


pyg.init()
scrn = pyg.display.set_mode(size)
clr = [0, 0, 0]

scrn.fill([0, 0, 0])

for i in range(size[0]*size[1]):
    
