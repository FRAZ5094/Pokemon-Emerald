import multiprocessing
import threading
from maps import *
import time
from main import *
import settings



def createMapNot(Class,q):
    q.put(Class(settings.screenScale,settings.scl))
    
def updateMapList():
    while True:
        settings.Maps.append(q.get())

if __name__ == '__main__':
    #settings.Maps.append(LittlerootTrainerTop(settings.screenScale,settings.scl))
    MapClasses=[LittlerootTrainerBot,LittlerootOutside]
    q=multiprocessing.Queue()
    for Class in MapClasses:
        p=multiprocessing.Process(target=createMapNot,args=(Class,q))
        p.start()

    t=threading.Thread(target=updateMapList)
    t.start()
    p5.run(frame_rate=45)
