import p5



def createMaps(scale,scl):
    Maps=[]
    print("Loading in maps...")
    Maps.append(LittlerootTrainerTop(scale,scl))
    Maps.append(LittlerootTrainerBot(scale,scl))
    Maps.append(LittlerootOutside(scale,scl))
    print("Finished loading maps")
    return Maps




class Map:

    def __init__(self,screenScale,scl):

        self.sprite=p5.load_image(self.spriteLocation)
        self.Upscaled=6
        self.gridWidth=int(self.sprite.size[0]/(self.Upscaled*16)-1)
        self.gridHeight=int(self.sprite.size[1]/(self.Upscaled*16)-1)


        self.screenScale=screenScale/self.Upscaled
        self.scl=scl
        self.pos=p5.Vector(0,0)
        self.lockedDir=p5.Vector(0,0)
        self.dir=p5.Vector(0,0)

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
        super().__init__(screenScale,scl)

    def __repr__(self):
        return "Littleroot Town Trainer House Bottom"
class LittlerootOutside(Map):

    def __init__(self,screenScale,scl):
     
        self.spriteLocation=r"Images\Maps\LittleRootTown\LittleRootTownOutside.png"

        self.gridpos=p5.Vector(10,10)

        self.bannedList=[]
        self.bannedfromDown=[]
        self.bannedfromUp=[]
        self.bannedfromRight=[]
        self.bannedfromLeft=[]

        self.extraSprite=p5.load_image(r"Images\Maps\LittleRootTown\TrainerHouseDownStairsExtraSprites.png")
        self.extraActiveCoords=[(1,4)]
        super().__init__(screenScale,scl)

    def __repr__(self):
        return "Littleroot Town"