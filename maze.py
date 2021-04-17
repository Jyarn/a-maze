import pygame as pyg
import random
import config
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
        pyg.draw.rect(config.screen, colour, [pos[0]*config.elmSz+config.elmSz, pos[1]*config.elmSz+config.wallSize, config.wallSize, config.pathSize])

    if fill.left:
        pyg.draw.rect(config.screen, colour, [pos[0]*config.elmSz, pos[1]*config.elmSz+config.wallSize, config.wallSize, config.pathSize])

    if fill.up:
        pyg.draw.rect(config.screen, colour, [pos[0]*config.elmSz+config.wallSize, pos[1]*config.elmSz, config.pathSize, config.wallSize])

    if fill.down:
        pyg.draw.rect(config.screen, colour, [pos[0]*config.elmSz+config.wallSize, pos[1]*config.elmSz+config.elmSz, config.pathSize, config.wallSize])

def pathFill(pos, colour): # fills inner squares
    pyg.draw.rect(config.screen, colour, [pos[0]*config.elmSz+config.wallSize, pos[1]*config.elmSz+config.wallSize, config.pathSize, config.pathSize])

def mazeCreate():
    # elm pattern for each element  
    config.screen.fill(config.colours[0])
    pyg.display.update()

    # 2d list init
    temp = [mzElm()]*int(config.size[1]/config.elmSz+1)
    mazeMap = [temp]*int(config.size[0]/config.elmSz+1)
    
    for x in range(len(mazeMap)): # init all list elements with a blank mzElm
        for y in range(len(temp)):
            temp[y] = mzElm()

        mazeMap[x] = temp
        temp = [mzElm()]*int(config.size[1]/config.elmSz)

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
            wallFill(mazeMap[x][y], config.colours[1], [x, y])
            pathFill([x, y], config.colours[1])
        pyg.display.flip()

