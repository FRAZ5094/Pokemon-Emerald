import p5 
import pyperclip
from maps import *
screenScale=1
scl=16*screenScale
Map=LittlerootTrainerTop(screenScale,scl)

def setup():
    p5.size(scl*20,scl*20)
    


def draw():
    p5.background(0)
    
    p5.image_mode("CORNER")
    p5.image(Map.sprite,(0,0),size=(Map.sprite.size[0]*screenScale/6,Map.sprite.size[1]*screenScale/6))

    if not True:
        p5.stroke(255)
        p5.no_fill()
        for x in range(int(width/16)):
            for y in range(int(height/16)):
                p5.begin_shape()
                p5.vertex(x*scl,y*scl)
                p5.vertex(x*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,(y+1)*scl)
                p5.vertex((x+1)*scl,y*scl)
                p5.end_shape()

    p5.rect_mode("CENTER")
    p5.fill(255,0,0,90)
    for x,y in Map.bannedList:
        p5.rect((x*scl+0.5*scl,y*scl+0.5*scl),scl,scl)

def key_pressed():
    if key=="ENTER":
        pyperclip.copy(str(Map.bannedList))
        spam = pyperclip.paste()
        print("bannedList added to clipboard")


def mouse_pressed():
    gridx=int(mouse_x/scl)
    gridy=int(mouse_y/scl)
    if not (gridx,gridy) in Map.bannedList:
        Map.bannedList.append((gridx,gridy))
    else:
        Map.bannedList.remove((gridx,gridy))


p5.run()