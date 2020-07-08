import p5
import time
import settings

class Map:

    def __init__(self,screenScale,scl):

        self.sprite=p5.load_image(self.spriteLocation)
        self.Upscaled=6
        self.gridWidth=int(self.sprite.size[0]/(self.Upscaled*16)-1)
        self.gridHeight=int(self.sprite.size[1]/(self.Upscaled*16)-1)


        self.screenScale=screenScale/self.Upscaled
        self.scl=scl
        self.pos=p5.Vector(0,0)
        self.lockedDir=0
        self.dir=0

        self.walkThroughWalls=False
        self.ExtraShowFirst=True

        print("Loaded Map: \"{}\"".format(self))
    
    def show(self):
        self.pos.x=width/2-self.gridpos.x*self.scl-self.scl*1/2
        self.pos.y=height/2-self.gridpos.y*self.scl-self.scl*9/32
        p5.image_mode("CORNER")
        p5.image(self.sprite,(self.pos.x,self.pos.y),size=(self.sprite.size[0]*self.screenScale,self.sprite.size[1]*self.screenScale))

    def GridtoPosX(self,gridposx):
        return (width/2-self.gridpos.x*self.scl-self.scl*1/2)+gridposx*self.scl
        
    def GridtoPosY(self,gridposy):
        return (height/2-self.gridpos.y*self.scl-self.scl*9/32)+gridposy*self.scl

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

        if player.walkTimer%player.walkingAnimationTime==9:
            self.gridpos.x=round(self.gridpos.x,0)
            self.gridpos.y=round(self.gridpos.y,0)
            self.checkIfDoor()

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

    def drawExtras(self):
        p5.image_mode("CORNER")
        showExtra=False
        for i in range(len(self.extraActiveCoords)):
            if self.gridpos.x>=self.extraActiveCoords[i][0]-0.9 and self.gridpos.x<=self.extraActiveCoords[i][0]+0.9 and self.gridpos.y>=self.extraActiveCoords[i][1]-0.9 and self.gridpos.y<=self.extraActiveCoords[i][1]+0.9:
                showExtra=True
                break
        if showExtra or self.ExtraShowFirst:
            p5.image(self.extraSprite,(self.GridtoPosX(0),self.GridtoPosY(0)),size=(self.extraSprite.size[0]*self.screenScale,self.extraSprite.size[1]*self.screenScale))
            self.ExtraShowFirst=False
    @staticmethod
    def changeMap(MapClass):

        for i,Class in enumerate(settings.Maps):
            if Class.__class__==MapClass:
                settings.currentMap=i
                return

    def checkIfDoor(self):
        if (int(self.gridpos.x),int(self.gridpos.y)) in self.DoorCoords:
            index=self.DoorCoords.index((int(self.gridpos.x),int(self.gridpos.y)))
            Map.changeMap(self.DoorDestination[index])




class LittlerootTrainerTop(Map):

    def __init__(self,screenScale,scl):
        
        self.spriteLocation=r"Images\Maps\LittleRootTown\TrainerHouseUpstairs.png"

        self.gridpos=p5.Vector(4,4)

        self.bannedList=[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (6, 0), (8, 0), (8, 1), (7, 0), (6, 1), (5, 0), (4, 1), (5, 1), (3, 1), (2, 1), (1, 1), (0, 1), (1, 5)]
        self.bannedfromDown=[]
        self.bannedfromUp=[]
        self.bannedfromRight=[]
        self.bannedfromLeft=[]

        self.extraSprite=p5.load_image(r"Images\Maps\LittleRootTown\TrainerHouseUpstairsExtraSprites.png")
        self.extraActiveCoords=[(1,4)]

        self.DoorCoords=[(7,1)]
        self.DoorDestination=[LittlerootTrainerBot]

        super().__init__(screenScale,scl)

    def __repr__(self):
        return "Littleroot Town Trainer House Top"


class LittlerootTrainerBot(Map):


    def __init__(self,screenScale,scl):
        
        self.spriteLocation=r"Images\Maps\LittleRootTown\TrainerHouseDownStairs.png"

        self.gridpos=p5.Vector(8,2)

        self.bannedList=[(7, 0), (6, 0), (6, 1), (5, 1), (5, 0), (4, 1), (3, 1), (2, 1), (1, 0), (4, 2), (3, 2), (2, 2), (1, 2), (4, 0), (3, 0), (2, 0), (0, 0), (0, 1), (1, 1), (0, 2), (8, 0), (9, 0), (10, 0), (2, 4), (3, 4), (4, 4), (3, 6), (4, 6), (4, 7), (3, 7), (7, 2), (7, 1), (9, 1), (10, 1), (10, 2), (9, 2), (8, 1)]
        self.bannedfromDown=[]
        self.bannedfromUp=[]
        self.bannedfromRight=[]
        self.bannedfromLeft=[]

        self.extraSprite=p5.load_image(r"Images\Maps\LittleRootTown\TrainerHouseDownStairsExtraSprites.png")
        self.extraActiveCoords=[(4,3)]

        self.DoorCoords=[(8,2),(8,8),(9,8)]
        self.DoorDestination=[LittlerootTrainerTop,LittlerootOutside,LittlerootOutside]



        super().__init__(screenScale,scl)

    def __repr__(self):
        return "Littleroot Town Trainer House Bottom"
class LittlerootOutside(Map):

    def __init__(self,screenScale,scl):
     
        self.spriteLocation=r"Images\Maps\LittleRootTown\LittleRootTownOutside.png"

        self.gridpos=p5.Vector(13,9)

        self.bannedList=[(8, 3), (9, 3), (9, 2), (9, 1), (10, 1), (11, 1), (13, 1), (12, 1), (14, 1), (15, 1), (17, 1), (16, 1), (20, 0), (20, 1), (17, 0), (23, 1), (21, 1), (22, 1), (24, 1), (25, 1), (26, 1), (26, 3), (26, 2), (27, 3), (28, 3), (28, 5), (28, 6), (28, 7), (28, 4), (28, 8), (28, 9), (28, 10), (28, 13), (28, 11), (28, 12), (28, 14), (28, 15), (28, 16), (27, 16), (26, 16), (26, 17), (26, 18), (24, 18), (25, 18), (24, 19), (24, 20), (23, 20), (22, 20), (21, 20), (20, 20), (19, 20), (18, 20), (15, 20), (16, 20), (14, 20), (17, 20), (13, 20), (12, 20), (11, 20), (10, 20), (9, 20), (9, 19), (9, 18), (8, 18), (7, 18), (7, 17), (7, 16), (7, 15), (7, 14), (7, 13), (7, 12), (7, 11), (7, 10), (7, 9), (7, 5), (7, 3), (7, 8), (7, 4), (7, 7), (7, 6), (10, 8), (11, 8), (12, 8), (14, 8), (14, 7), (13, 7), (12, 7), (14, 6), (12, 6), (11, 6), (13, 6), (11, 7), (10, 7), (10, 6), (21, 6), (22, 6), (23, 6), (24, 6), (25, 6), (21, 7), (22, 7), (23, 7), (25, 7), (24, 8), (25, 8), (23, 8), (21, 8), (24, 7), (20, 8), (23, 13), (15, 8), (17, 16), (17, 13), (17, 14), (16, 13), (13, 13), (12, 13), (12, 14), (15, 13), (14, 13), (16, 14), (15, 14), (14, 14), (13, 14), (11, 13), (11, 14), (11, 16), (11, 15), (16, 15), (13, 15), (14, 17), (14, 15), (15, 15), (17, 15), (14, 16), (13, 16), (12, 16), (12, 15), (16, 16)]
        self.bannedfromDown=[]
        self.bannedfromUp=[]
        self.bannedfromRight=[]
        self.bannedfromLeft=[]

        self.extraSprite=p5.load_image(r"Images\Maps\LittleRootTown\TrainerHouseDownStairsExtraSprites.png")
        self.extraActiveCoords=[(0,0)]


        self.DoorCoords=[(13,8)]
        self.DoorDestination=[LittlerootTrainerBot]
        super().__init__(screenScale,scl)







    def __repr__(self):
        return "Littleroot Town"