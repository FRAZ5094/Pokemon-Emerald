import p5
import math
def createMaps(scale,scl):
    Maps=[]
    Maps.append(Map(r"Images\Maps\LittleRootTown\TrainerHouseUpstairs.png",scale,scl))

    return Maps

class Map:

    def __init__(self,spriteLocation,screenScale,scl):
        self.sprite=p5.load_image(spriteLocation)
        Upscaled=6
        self.screenScale=screenScale/Upscaled
        self.scl=scl

        self.gridWidth=8
        self.gridHeight=7
        self.bannedList=[(4,4)]

        self.gridpos=p5.Vector(4,5)
        self.pos=p5.Vector(0,0)
        self.dir=p5.Vector(0,0)

        self.walkThroughWalls=False


    def show(self):
        self.pos.x=width/2-self.gridpos.x*self.scl-self.scl*1/2
        self.pos.y=height/2-self.gridpos.y*self.scl-self.scl*9/32
        p5.image_mode("CORNER")
        p5.image(self.sprite,(self.pos.x,self.pos.y),size=(self.sprite.size[0]*self.screenScale,self.sprite.size[1]*self.screenScale))



    def move(self,player):

        if player.walkTimer%player.walkingAnimationTime==0:
            self.lockedDir=self.dir
            player.spriteNo=self.lockedDir

        if self.canMoveUp() and self.lockedDir==0:
            self.gridpos.y+=-1/player.walkingAnimationTime

        elif self.canMoveRight() and self.lockedDir==1:
            self.gridpos.x+=1/player.walkingAnimationTime

        elif self.canMoveDown() and self.lockedDir==2:
            self.gridpos.y+=1/player.walkingAnimationTime

        elif self.canMoveLeft() and self.lockedDir==3:
            self.gridpos.x+=-1/player.walkingAnimationTime

        player.walkTimer+=1




    def canMoveUp(self):
        if not self.walkThroughWalls:
            return self.gridpos.y>0.1 and ((int(self.gridpos.x),int(self.gridpos.y-0.01)) not in self.bannedList)
        else:
            return True
    def canMoveRight(self):
        if not self.walkThroughWalls:
            return self.gridpos.x+0.1<self.gridWidth and ((int(self.gridpos.x+1),int(self.gridpos.y)) not in self.bannedList)
        else:
            return True

    def canMoveDown(self):
        if not self.walkThroughWalls:
            return self.gridpos.y+0.1<self.gridHeight and ((int(self.gridpos.x),int(self.gridpos.y+1)) not in self.bannedList)
        else:
            return True
  

    def canMoveLeft(self):
        if not self.walkThroughWalls:
            return self.gridpos.x>0.1 and ((int(self.gridpos.x-0.01),int(self.gridpos.y)) not in self.bannedList)
        else:
            return True
 
 