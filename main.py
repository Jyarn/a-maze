import pygame as pyg
import random
import time
import sys

class mzElm(): # maze element
    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.init = False

    def dirSet(self, up = False, down = False, right = False, left = False): # debug
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.init = True
        return self


def end(): # cleanup
    print("done")

def elmFill(fill, colour, pos):
    if fill.right:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])

    if fill.left:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])

    if fill.up:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz, pathSize, wallSize])

    if fill.down:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz+elmSz, pathSize, wallSize])

def pathFill(pos, colour):
    pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz+wallSize, pathSize, pathSize])


wallSize = 1; 
pathSize = 20;

elmSz = wallSize + pathSize
pattern = [0]*wallSize + [1]*pathSize

colours = [ [64, 0, 0], [0, 0, 0] ]


monRes = [1920, 1080]

# elm pattern for each element
size = [ monRes[0]+(monRes[0]%elmSz), monRes[1]+(monRes[1]%elmSz)]


pyg.init()
screen = pyg.display.set_mode(size)

screen.fill(colours[1])


# create grid
for x in range(size[0]):
    if pattern[x%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [x, 0], [x, size[1]])
        pyg.display.flip()

for y in range(size[1]):
    if pattern[y%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [0, y], [size[0], y])
        pyg.display.flip()

# 2d list init
temp = [mzElm()]*int(size[1]/elmSz+1)
mazeMap = [temp]*int(size[0]/elmSz+1)

for x in range(len(mazeMap)): # init all list elements with a blank mzElm
    for y in range(len(temp)):
        temp[y] = mzElm()

    mazeMap[x] = temp
    temp = [mzElm()]*int(size[1]/elmSz)

# stack because recursions for losers
stack = [[random.randint(0, int(size[0]/elmSz)), random.randint(0, int(size[1]/elmSz))]]
dirs = [0, 1, 2, 3] # keeps track of directions 

while True:
    pyg.event.clear() # clear event queue so windows doesn't freeze
    i = random.randrange(len(dirs)) # choose a random number 
    Dir = dirs[i]

    if Dir == 0 and stack[-1][1] != 0 and mazeMap[stack[-1][0]][stack[-1][1]-1].init == False: #up
        mazeMap[stack[-1][0]][stack[-1][1]].up = True
        stack.append([stack[-1][0], stack[-1][1]-1])
        
    elif Dir == 1 and stack[-1][0]+2 != len(mazeMap) and mazeMap[stack[-1][0]+1][stack[-1][1]].init == False: # right
        mazeMap[stack[-1][0]][stack[-1][1]].right = True
        stack.append([stack[-1][0]+1, stack[-1][1]])

    elif Dir == 2 and stack[-1][1]+2 != len(mazeMap[0]) and mazeMap[stack[-1][0]][stack[-1][1]+1].init == False: # Down
        mazeMap[stack[-1][0]][stack[-1][1]].down = True
        stack.append([stack[-1][0], stack[-1][1]+1])

    elif stack[-1][0] != 0 and mazeMap[stack[-1][0]-1][stack[-1][1]].init == False: # left
        mazeMap[stack[-1][0]][stack[-1][1]].left = True
        stack.append([stack[-1][0]-1, stack[-1][1]])

    elif len(dirs) == 0: 
        stack.pop()

    else:
        dirs.remove(Dir)
        
        if len(dirs) == 0:
            stack.pop()
        
        else: 
            continue

    if len(stack) == 0:
        break

    mazeMap[stack[-1][0]][stack[-1][1]].init = True # mark current elm as init
    dirs = [0, 1, 2, 3] # refresh list

# render maze
for x in range(len(mazeMap)-1):
    for y in range(len(mazeMap[0])-1):
        elmFill(mazeMap[x][y], colours[1], [x, y])
        pyg.event.clear()

    pyg.display.flip() # idk looks cool or something

# event handler
while True:
    for evn in pyg.event.get():
        if evn.type == pyg.QUIT:
            end()
            sys.exit()

    key = pyg.key.get_pressed()
    if key[pyg.K_q] == True:
        end()
        sys.exit()

    pyg.display.flip()
