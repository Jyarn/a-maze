import pygame as pyg
import random
import time
import sys

class mzElm(): # maze table element
    up = False # up
    dwn = False # down
    rt = False # right
    lt = False # left

def end(): # cleanup
    print("done")


# wall to path ratio
wallSize = 1; 
pathSize = 5;

pattern = [0]*wallSize + [1]*pathSize;

# colours[0] = wall colour
# colours[1] = path colour
# colours[2] = background colour
colours = [ [64, 0, 0], [0, 0, 0], [0, 0, 0] ]


monRes = [1920, 1080] # monitor res
border = [0, 0] # border size 0 = fullscreen
size = [monRes[0]-border[0], monRes[1]-border[1]] # window size based on monRes and border size


pyg.init()
screen = pyg.display.set_mode(size)

screen.fill(colours[2])


for x in range(size[0]):
    if pattern[x%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [x, 0], [x, size[1]]) # alternate between colours 1/2 according to pattern
        time.sleep(0.001)
        pyg.display.flip()
    

for y in range(size[1]):
    if pattern[y%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [0, y], [size[0], y]) # same
        time.sleep(0.001)
        pyg.display.flip()
    

while True: # event handler
    for evn in pyg.event.get(): # handles program exits
        if evn.type == pyg.QUIT:
            end()
            sys.exit()

    key = pyg.key.get_pressed()
    if key[pyg.K_q] == True: # handles keyboard events
        end()
        sys.exit()

    pyg.display.flip()
