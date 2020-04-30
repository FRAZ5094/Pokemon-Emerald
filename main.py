import p5
import math
import multiprocessing as mp
import threading
from pynput import keyboard
from player import *
from maps import *


screenScale=5
scl=16*screenScale

global Maps
Maps=[]

showGrid=False
currentMap=0
player=Player(1,2,screenScale)

def runP5():
    p5.run(frame_rate=45)


def createMapObj(Class):

    print("Loading map")
    q.put(Class(screenScale,scl))
    
def updateMapList():

    while True:
        Maps.append(q.get())
        print("loaded a map")



def on_release(Key):
    global lastKey,player
    if str(Key)=="Key.up" or str(Key)=="Key.down" or str(Key)=="Key.right" or str(Key)== "Key.left":
        if str(Key)==lastKey:
            player.stopRequest=True

listener = keyboard.Listener(on_release=on_release)
listener.start()



def setup():
    global Maps
    p5.size(screenScale*240,screenScale*160)

def draw():
    p5.background(0)

    if player.walking:
        Maps[currentMap].move(player)
        player.walkingAnimation(Maps[currentMap])
        if player.walkTimer%player.walkingAnimationTime==0 and player.stopRequest:
            player.walking=False
            player.walkTimer=0

    Maps[currentMap].show()
    player.show()
    Maps[currentMap].drawExtras()

    p5.stroke(255)
    p5.stroke_weight(1)
    if showGrid:
        for x in range(Maps[currentMap].gridWidth+2):
            p5.line((Maps[currentMap].GridtoPosX(x),Maps[currentMap].GridtoPosY(0)),(Maps[currentMap].GridtoPosX(x),Maps[currentMap].GridtoPosY(Maps[currentMap].gridHeight+1)))
        for y in range(Maps[currentMap].gridHeight+2):
            p5.line((Maps[currentMap].GridtoPosX(0),Maps[currentMap].GridtoPosY(y)),(Maps[currentMap].GridtoPosX(Maps[currentMap].gridWidth+1),Maps[currentMap].GridtoPosY(y)))




def key_pressed():
    global showGrid,lastKey,currentMap

    if key=="UP":
        lastKey="Key.up"
        if player.walking and Maps[currentMap].dir==0:
            player.stopRequest=True
        else:
            Maps[currentMap].dir=0
            player.walking=True
            player.stopRequest=False

    if key=="RIGHT":
        lastKey="Key.right"
        if player.walking and Maps[currentMap].dir==1:
            player.stopRequest=True
        else:
            Maps[currentMap].dir=1
            player.walking=True
            player.stopRequest=False

    if key=="DOWN":
        lastKey="Key.down"
        if player.walking and Maps[currentMap].dir==2:
            player.stopRequest=True
        else:
            Maps[currentMap].dir=2
            player.walking=True
            player.stopRequest=False

    if key=="LEFT":
        lastKey="Key.left"
        if player.walking and Maps[currentMap].dir==3:
            player.stopRequest=True
        else:
            Maps[currentMap].dir=3
            player.walking=True
            player.stopRequest=False

    if key=="ENTER":
        #Maps[currentMap].gridpos=p5.Vector(2,2)
        print(Maps[currentMap].gridpos.x,Maps[currentMap].gridpos.y)
    if key=="#":
        if not showGrid:
            showGrid=True
        else:
            showGrid=False
    if key=="]":
        if not Maps[currentMap].walkThroughWalls:
            Maps[currentMap].walkThroughWalls=True
            print("Walk through walls on")
        else:
            Maps[currentMap].walkThroughWalls=False
            print("Walk through walls off")
    if key=="1":
        currentMap=0
    if key=="2":
        currentMap=1
    if key=="3":
        currentMap=2

