import pygame as pyg
import random
import time
import sys

class mzElm(): # maze table element
    def __init__(self):
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.init = False

    def dirSet(self, up = False, down = False, right = False, left = False):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.init = True
        return self



def end(): # cleanup
    print("done")

def elmFill(fill, colour, pos):
    print(pos, end = "")
    if fill.right:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])
        print("right | ", end = "")

    if fill.left:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz, pos[1]*elmSz+wallSize, wallSize, pathSize])
        print("left | ", end = "")

    if fill.up:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz, pathSize, wallSize])
        print("up | ", end = "")

    if fill.down:
        pyg.draw.rect(screen, colour, [pos[0]*elmSz+wallSize, pos[1]*elmSz+elmSz, pathSize, wallSize])
        print("down |", end = "")

    print("\n")
# wall to path ratio
wallSize = 10; 
pathSize = 20;

elmSz = wallSize + pathSize
pattern = [0]*wallSize + [1]*pathSize

# colours[0] = wall colour
# colours[1] = path colour
# colours[2] = background colour
colours = [ [64, 0, 0], [0, 0, 0], [0, 0, 0] ]


monRes = [1920, 1080] # monitor res
border = [0, 0] # border size 0 = fullscreen

#probably should improve this
size = [ monRes[0]+(monRes[0]%elmSz), monRes[1]+(monRes[1]%elmSz)] # window size based on monRes and border size


pyg.init()
screen = pyg.display.set_mode(size)

screen.fill(colours[2])

print("Broken build. Don't use")
for x in range(size[0]): # replace w/ draw.rect
    if pattern[x%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [x, 0], [x, size[1]]) # alternate between colours 1/2 according to pattern
        pyg.display.flip()

for y in range(size[1]):
    if pattern[y%(pathSize + wallSize)] == 0:
        pyg.draw.line(screen, colours[0], [0, y], [size[0], y]) # same
        pyg.display.flip()


# type declaration for smart people (<1 000 000 iq not welcome)
temp = [mzElm()]*int(size[1]/elmSz)
mazeMap = [temp]*int(size[0]/elmSz)
# you see python is a simple language, this is why we don't have type declaration because 101% of the you won't have to use lists at all not at all

for x in range(len(mazeMap)):
    for y in range(len(temp)):
        temp[y] = mzElm()

    mazeMap[x] = temp
    temp = [mzElm()]*int(size[1]/elmSz)

stack = [[random.randint(0, size[0]/elmSz), random.randint(0, size[1]/elmSz)]]
dirs = [0, 1, 2, 3]

while len(stack) != 0:
    # gen random number
    i = random.randrange(len(dirs))
    Dir = dirs[i]
    
    #print(stack[-1], len(mazeMap), len(mazeMap[0]))
    # check next elm if init
    print(len(stack), len(dirs))
    if Dir == 0 and stack[-1][1] != 1 and mazeMap[stack[-1][0]][stack[-1][1]-1].init == False: #up
        stack.append([stack[-1][0], stack[-1][1]-1])
        mazeMap[stack[-1][0]][stack[-1][1]].up = True

    elif Dir == 1 and stack[-1][0]+3 != len(mazeMap) and mazeMap[stack[-1][0]+1][stack[-1][1]].init == False: # right
        stack.append([stack[-1][0]+1, stack[-1][1]])
        mazeMap[stack[-1][0]][stack[-1][1]].right = True

    elif Dir == 2 and stack[-1][1]+3 != len(mazeMap[0]) and mazeMap[stack[-1][0]][stack[-1][1]+1].init == False: # Down
        stack.append([stack[-1][0], stack[-1][1]+1])
        mazeMap[stack[-1][0]][stack[-1][1]].down = True

    elif stack[-1][0] != 1 and mazeMap[stack[-1][0]-1][stack[-1][1]].init == False: # left
        stack.append([stack[-1][0]-1, stack[-1][1]])
        mazeMap[stack[-1][0]][stack[-1][1]].left = True

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

    mazeMap[stack[-1][0]][stack[-1][1]].init = True
    dirs = [0, 1, 2, 3]
    # scroll pos
    
    # update mzElm


for x in range(len(mazeMap)-1):
    for y in range(len(mazeMap[0])-1):
        elmFill(mazeMap[x][y], [255, 255, 255], [x, y])
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
