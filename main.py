import p5
from player import *
from maps import *

global screenScale,scl
screenScale=4
scl=16*screenScale
player=Player(1,2,screenScale)



def setup():
    global Maps
    p5.size(screenScale*240,screenScale*160)
    Maps=createMaps(screenScale,scl)


def draw():
    global Maps
    p5.background(0)



    Maps[0].show()
    p5.stroke(255)
    p5.no_fill()
    for x in range(len(Maps[0].grid)):
        
        for y in range(len(Maps[0].grid[0])):
            p5.begin_shape()
            p5.vertex(x*scl,y*scl)
            p5.vertex(x*scl,(y+1)*scl)
            p5.vertex((x+1)*scl,(y+1)*scl)
            p5.vertex((x+1)*scl,y*scl)
            p5.end_shape()
    player.show()

def key_pressed():
    if key=="UP":
        player.spriteNo=0
        Maps[0].moveUp()
    if key=="RIGHT":
        player.spriteNo=1
        Maps[0].moveRight()
    if key=="DOWN":
        player.spriteNo=2
        Maps[0].moveDown()
    if key=="LEFT":
        player.spriteNo=3
        Maps[0].moveLeft()


p5.run()