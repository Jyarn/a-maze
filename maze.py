import pygame as pyg
import random
import time
import sys
import _thread

class mzElm(): # maze element
    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.init = False

    def dirSet(self, up = False, down = False, right = False, left = False):
        """set a direction and returns self only for creating a fresh element mzElm().dirSet()"""
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.init = True
        return self

def wallFill(fill, colour, pos): # fills walls
    if fill.right:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])

    if fill.left:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])

    if fill.up:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz, pathSize, wallSize])

    if fill.down:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz+elmSz, pathSize, wallSize])

def pathFill(pos, colour): # fills inner squares
    pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz+wallSize, pathSize, pathSize])


def waitForExit():
    global end
    input("Press any key to exit... ")
    end = True
    
end = False

wallSize = 1
pathSize = 25

elmSz = wallSize + pathSize     # element size 

# 0 = wall colour
# 1 = path colour
colours = [ [128, 0, 0], [0, 0, 0] ]


#add border
winRes = [720, 720]

# elm pattern for each element
size = [ int(winRes[0] / elmSz) * elmSz+wallSize, int(winRes[1] / elmSz) * elmSz+wallSize] # window size 
pyg.display.set_caption("Window Resolution" + str(size[0]) + " x " + str(size[1]))

pyg.init()
screen = pyg.display.set_mode(size)

screen.fill(colours[0])
pyg.display.update()

def mazeCreate():
    # 2d list init
    temp = [mzElm()]*int(size[1]/elmSz+1)
    mazeMap = [temp]*int(size[0]/elmSz+1)
    
    for x in range(len(mazeMap)): # init all list elements with a blank mzElm
        for y in range(len(temp)):
            temp[y] = mzElm()

        mazeMap[x] = temp
        temp = [mzElm()]*int(size[1]/elmSz)

    # stack because recursions for losers
    stack = [[random.randint(0, len(mazeMap)-2), random.randint(0, len(mazeMap[0])-2)]]
    mazeMap[stack[-1][0]][stack[-1][1]].init = True
    dirs = [0, 1, 2, 3] # optional directions

    while True:
        pyg.event.pump()    # default event handler
        i = random.randrange(len(dirs)) # choose a random number 
        Dir = dirs[i]

        # checks directions (Dir == 0)
        # if it's in bounds (stack[-1][1] != 0)
        # and if it's initialized (mazeMap[stack[-1][0]][stack[-1][1]-1].init == False)
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

        else:
            # marks direction as invalid
            dirs.remove(Dir)
            
            if len(dirs) == 0:
                stack.pop()
            
            else: 
                continue

        if len(stack) == 0: # loop condition
            break

        mazeMap[stack[-1][0]][stack[-1][1]].init = True # mark current elm as init
        dirs = [0, 1, 2, 3] # refresh list


    # render maze
    for x in range(len(mazeMap)-1):
        for y in range(len(mazeMap[0])-1):
            wallFill(mazeMap[x][y], colours[1], [x, y])
            pathFill([x, y], colours[1])
        pyg.display.flip()


# event handler
mazeCreate()
_thread.start_new_thread(waitForExit)
while True: # multi thread
    for evn in pyg.event.get():
        if evn.type == pyg.QUIT:
            end()
            sys.exit()

    if end:
        sys.exit()

    pyg.event.pump()
    pyg.display.flip()
