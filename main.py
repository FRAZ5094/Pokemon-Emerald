import p5
import math
from pynput import keyboard
from player import *
from maps import *

screenScale=5
scl=16*screenScale
showGrid=False
player=Player(1,2,screenScale)

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
    Maps=createMaps(screenScale,scl)


def draw():
    global Maps,showGrid
    p5.background(0)
    Maps[0].show()

    if showGrid:
        p5.stroke(255)
        p5.no_fill()
        for x in range(Maps[0].gridWidth+1):
            x+=(width/2)/scl-Maps[0].gridpos.x-0.5
            for y in range(Maps[0].gridHeight+1):
                y+=(height/2)/scl-Maps[0].gridpos.y-9/32
                p5.begin_shape()
                p5.vertex(x*scl,y*scl)
                p5.vertex(x*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,y*scl)
                p5.end_shape()

    if player.walking:
        Maps[0].move(player)
        player.walkingAnimation(Maps[0])
        if player.walkTimer%player.walkingAnimationTime==0 and player.stopRequest:
            player.walking=False
            player.walkTimer=0
            Maps[0].gridpos.x=round(Maps[0].gridpos.x,0)
            Maps[0].gridpos.y=round(Maps[0].gridpos.y,0)
    p5.fill(255,0,0,70)

    p5.rect((4*scl+scl*((width/2)/scl-Maps[0].gridpos.x-0.5),4*scl+scl*((height/2)/scl-Maps[0].gridpos.y-9/32)),scl,scl)
    player.show()
    print(Maps[0].gridpos.x,Maps[0].gridpos.y)

def key_pressed():
    global Maps,showGrid,lastKey

    if key=="UP":
        lastKey="Key.up"
        if player.walking and Maps[0].dir==0:
            player.stopRequest=True
        else:
            Maps[0].dir=0
            player.walking=True
            player.stopRequest=False
   
    if key=="RIGHT":
        lastKey="Key.right"
        if player.walking and Maps[0].dir==1:
            player.stopRequest=True
        else:
            Maps[0].dir=1
            player.walking=True
            player.stopRequest=False
   
    if key=="DOWN":
        lastKey="Key.down"
        if player.walking and Maps[0].dir==2:
            player.stopRequest=True
        else:
            Maps[0].dir=2
            player.walking=True
            player.stopRequest=False

    if key=="LEFT":
        lastKey="Key.left"
        if player.walking and Maps[0].dir==3:
            player.stopRequest=True
        else:
            Maps[0].dir=3
            player.walking=True
            player.stopRequest=False

    if key=="ENTER":
        Maps[0].gridpos=p5.Vector(2,2)
    if key=="#":
        if not showGrid:
            showGrid=True
        else:
            showGrid=False
    if key=="]":
        if not Maps[0].walkThroughWalls:
            Maps[0].walkThroughWalls=True
            print("Walk through walls on")
        else:
            Maps[0].walkThroughWalls=False
            print("Walk through walls off")

p5.run(frame_rate=50)