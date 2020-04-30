import multiprocessing
import threading
from maps import *
import time
from main import runP5
import globals




def createMapNot(Class,q):
    q.put(Class(globals.screenScale,globals.scl))
    
def updateMapList():
    while True:
        globals.Maps.append(q.get())

if __name__ == '__main__':
    globals.Maps.append(LittlerootTrainerBot(globals.screenScale,globals.scl))
    MapClasses=[LittlerootTrainerBot,LittlerootOutside]
    q=multiprocessing.Queue()
    for Class in MapClasses:
        p=multiprocessing.Process(target=createMapNot,args=(Class,q))
        p.start()

    t=threading.Thread(target=updateMapList)
    t.start()
    runP5()
