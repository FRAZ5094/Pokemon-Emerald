
from maps import *

def initialize():

    global screenScale,scl,Maps
    screenScale=5
    scl=16*screenScale
    Maps=[]
    Maps.append(LittlerootTrainerTop(screenScale,scl))
