import p5
import numpy as np
def createMaps(scale,scl):
    Maps=[]
    Maps.append(Map(r"Images\Maps\LittleRootTown\TrainerHouseUpstairs.png",scale,scl))

    return Maps

class Map:

    def __init__(self,spriteLocation,screenScale,scl):
        self.grid=np.zeros((9,8))
        self.gridpos=p5.Vector(0,0)
        self.pos=p5.Vector(0,0)
        self.sprite=p5.load_image(spriteLocation)
        self.screenScale=screenScale/6
        self.scl=scl

    def show(self):
        self.pos.x=width/2-self.gridpos.x*self.scl-self.scl*1/2
        self.pos.y=height/2-self.gridpos.y*self.scl-self.scl*9/32
        p5.image_mode("CORNER")
        p5.image(self.sprite,(self.pos.x,self.pos.y),size=(self.sprite.size[0]*self.screenScale,self.sprite.size[1]*self.screenScale))

    def moveUp(self):
        self.gridpos.y-=1
    def moveDown(self):
        self.gridpos.y+=1
    def moveLeft(self):
        self.gridpos.x-=1
    def moveRight(self):
        self.gridpos.x+=1