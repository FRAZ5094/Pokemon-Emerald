import p5
import math
import multiprocessing as mp
import threading
from pynput import keyboard
from player import *
from maps import *
import settings

settings.initialize()


showGrid=False
currentMap=0
player=Player(1,2,settings.screenScale)



def on_released(Key):
    global lastKey,player
    print("running key released")
    if str(Key)=="Key.up" or str(Key)=="Key.down" or str(Key)=="Key.right" or str(Key)== "Key.left":
        if str(Key)==lastKey:
            player.stopRequest=True




def setup():
    p5.size(settings.screenScale*240,settings.screenScale*160)
    listener = keyboard.Listener(on_release=on_released)
    listener.start()


def draw():
    p5.background(0)

    if player.walking:
        settings.Maps[currentMap].move(player)
        player.walkingAnimation(settings.Maps[currentMap])
        if player.walkTimer%player.walkingAnimationTime==0 and player.stopRequest:
            player.walking=False
            player.walkTimer=0

    settings.Maps[currentMap].show()
    player.show()
    settings.Maps[currentMap].drawExtras()

    p5.stroke(255)
    p5.stroke_weight(1)
    if showGrid:
        for x in range(settings.Maps[currentMap].gridWidth+2):
            p5.line((settings.Maps[currentMap].GridtoPosX(x),settings.Maps[currentMap].GridtoPosY(0)),(settings.Maps[currentMap].GridtoPosX(x),settings.Maps[currentMap].GridtoPosY(settings.Maps[currentMap].gridHeight+1)))
        for y in range(settings.Maps[currentMap].gridHeight+2):
            p5.line((settings.Maps[currentMap].GridtoPosX(0),settings.Maps[currentMap].GridtoPosY(y)),(settings.Maps[currentMap].GridtoPosX(settings.Maps[currentMap].gridWidth+1),settings.Maps[currentMap].GridtoPosY(y)))

    print(settings.Maps)


def key_pressed():
    global showGrid,lastKey,currentMap

    if key=="UP":
        lastKey="Key.up"
        if player.walking and settings.Maps[currentMap].dir==0:
            player.stopRequest=True
        else:
            settings.Maps[currentMap].dir=0
            player.walking=True
            player.stopRequest=False

    if key=="RIGHT":
        lastKey="Key.right"
        if player.walking and settings.Maps[currentMap].dir==1:
            player.stopRequest=True
        else:
            settings.Maps[currentMap].dir=1
            player.walking=True
            player.stopRequest=False

    if key=="DOWN":
        lastKey="Key.down"
        if player.walking and settings.Maps[currentMap].dir==2:
            player.stopRequest=True
        else:
            settings.Maps[currentMap].dir=2
            player.walking=True
            player.stopRequest=False

    if key=="LEFT":
        lastKey="Key.left"
        if player.walking and settings.Maps[currentMap].dir==3:
            player.stopRequest=True
        else:
            settings.Maps[currentMap].dir=3
            player.walking=True
            player.stopRequest=False

    if key=="ENTER":
        #Maps[currentMap].gridpos=p5.Vector(2,2)
        print(settings.Maps[currentMap].gridpos.x,settings.Maps[currentMap].gridpos.y)
    if key=="#":
        if not showGrid:
            showGrid=True
        else:
            showGrid=False
    if key=="]":
        if not settings.Maps[currentMap].walkThroughWalls:
            settings.Maps[currentMap].walkThroughWalls=True
            print("Walk through walls on")
        else:
            settings.Maps[currentMap].walkThroughWalls=False
            print("Walk through walls off")
    if key=="1":
        currentMap=0
    if key=="2":
        currentMap=1
    if key=="3":
        currentMap=2



#p5.run(frame_rate=45)
