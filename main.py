import p5
from player import *
from maps import *


screenScale=6
scl=16*screenScale
showGrid=False
player=Player(1,2,screenScale)



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
        for x in range(len(Maps[0].grid[0])+1):
            x+=(width/2)/scl-Maps[0].gridpos.x-0.5
            for y in range(len(Maps[0].grid)+1):
                y+=(height/2)/scl-Maps[0].gridpos.y-9/32
                p5.begin_shape()
                p5.vertex(x*scl,y*scl)
                p5.vertex(x*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,y*scl)
                p5.end_shape()

    player.show()
    #print(Maps[0].gridpos)

def key_pressed():
    global Maps,showGrid
    if key=="UP":
        player.spriteNo=0
        if Maps[0].gridpos.y>0:
            Maps[0].gridpos.y-=1
    if key=="RIGHT":
        player.spriteNo=1
        if Maps[0].gridpos.x<(len(Maps[0].grid[0])):
            Maps[0].gridpos.x+=1
    if key=="DOWN":
        player.spriteNo=2
        if Maps[0].gridpos.y<len(Maps[0].grid):
            Maps[0].gridpos.y+=1
    if key=="LEFT":
        player.spriteNo=3
        if Maps[0].gridpos.x>0:
            Maps[0].gridpos.x-=1
    if key=="ENTER":
        Maps[0].gridpos=p5.Vector(2,2)
    if key=="#":
        if not showGrid:
            showGrid=True
        else:
            showGrid=False


p5.run(frame_rate=60)