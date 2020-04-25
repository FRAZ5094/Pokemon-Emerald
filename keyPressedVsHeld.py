import p5
from player import *

screenScale=6
scl=16*screenScale
pressedTime=-10000
player=Player(1,2,screenScale)

def setup():
    p5.size(600,600)



def draw():
    global pressedTime
    p5.background(0)

    if frame_count>=pressedTime+5:
        if player.spriteNo==5:
            player.spriteNo=0
        elif player.spriteNo==7:
            player.spriteNo=1
        if player.spriteNo==9:
            player.spriteNo=2
        if player.spriteNo==11:
            player.spriteNo=3

    if key_is_pressed and key=="DOWN" and frame_count>=pressedTime+10 and frame_count<=pressedTime+60:
        print("held")

    #print(frame_count,pressedTime)

    player.show()

def key_pressed():
    global pressedTime

    if key=="UP":
        pressedTime=frame_count
        if not player.spriteNo==5:
            player.dir=p5.Vector()
    if key=="RIGHT":
        pressedTime=frame_count
        if not player.spriteNo==7:
            player.turnRight()
    if key=="DOWN":
        print("pressed")
        pressedTime=frame_count
        if not player.spriteNo==9:
            player.turnDown()
    if key=="LEFT":
        pressedTime=frame_count
        if not player.spriteNo==11:
            player.turnLeft()


def key_released():
    global pressedTime
    print(key)
    pressedTime=0




p5.run(frame_rate=60)

