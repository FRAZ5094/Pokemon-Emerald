import p5
from player import *
global scale
scale=1
player=Player(1,2,scale)


def setup():
    p5.size(scale*240,scale*160)



def draw():
    p5.background(0)
    player.show()
    


def key_pressed():
    if key=="UP":
        player.spriteNo=0
    if key=="RIGHT":
        player.spriteNo=1
    if key=="DOWN":
        player.spriteNo=2
    if key=="LEFT":
        player.spriteNo=3


p5.run()