from maze import *
from event import *
import config
import _thread
import time

class eventProps:
    usrIn = "nothing lol"


pyg.init()
evntRet = eventProps()

def reset():
    global evntRet
    print("resetting...")
    evntRet.usrIn = "nothing lol"

# event handler
while True: # multi thread
    for evn in pyg.event.get():
        if evn.type == pyg.QUIT:
            sys.exit()

    if evntRet.usrIn == "start":
        config.screen = pyg.display.set_mode(config.size)
        pyg.display.set_caption("Window Resolution" + str(config.size[0]) + " x " + str(config.size[1]))
        
        print("starting maze generation...")
        mazeCreate()

        print("done maze generation")
        reset()

    elif evntRet.usrIn == "s":
        lock = True
        reset()

    elif evntRet.usrIn == "q":
        sys.exit()

    elif evntRet.usrIn == "cS":
        print("wwwww")
        reset()

    elif evntRet.usrIn == "cW":
        print("wwwww")
        reset()

    elif evntRet.usrIn == "cP":
        print("wwwww")
        reset()

    if evntRet.usrIn == "nothing lol":
        evntRet.usrIn = "pending"
        _thread.start_new_thread(askForInput, (evntRet,))

    pyg.event.pump()
    if config.screen != None:
        pyg.display.flip()