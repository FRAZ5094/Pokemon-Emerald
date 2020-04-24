import p5
from player import *
from maps import *


screenScale=5
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


    if key_is_pressed:
        print("adcasd")
        player.stopRequest=False
    else:
        player.stopRequest=True

    if player.walking:
        Maps[0].move(player)
        #player.WakingAnimation()
        if player.walkTimer%player.walkingAnimationTime==0 and player.stopRequest:
            print("Tried to stop")
            player.walking=False
            player.stopRequest=False
            player.walkTimer=0

    #print(player.walkTimer)
    #print(player.stopRequest)

    player.show()
    #print(Maps[0].gridpos)

def key_pressed():
    global Maps,showGrid

    if key=="UP":
        #player.spriteNo=0
        Maps[0].dir=0
        player.walking=True
        player.stopRequest=False
        return
    if key=="RIGHT":
        #player.spriteNo=1
        Maps[0].dir=1
        player.walking=True
        player.stopRequest=False
        return
    if key=="DOWN":
        #player.spriteNo=2
        Maps[0].dir=2
        player.walking=True
        player.stopRequest=False
        return
    if key=="LEFT":
        #player.spriteNo=3
        Maps[0].dir=3
        player.walking=True
        player.stopRequest=False
        return
    if key=="ENTER":
        Maps[0].gridpos=p5.Vector(2,2)
    if key=="#":
        if not showGrid:
            showGrid=True
        else:
            showGrid=False

    
def key_released():
        #player.stopRequest=True
        pass


p5.run(frame_rate=60)