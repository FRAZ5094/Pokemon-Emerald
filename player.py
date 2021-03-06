import p5
from time import sleep
class Player:


    def __init__(self,gender,sprite,screenScale):
        
        self.gender=gender
        self.spriteNo=sprite
        Upscaled=6
        self.screenScale=screenScale/Upscaled
        
        self.walking=False
        self.walkTimer=0
        self.walkingAnimationTime=10
        self.walkingProgress=0
        self.stopRequest=False
        self.Right=True


        self.Sprites=[]
        if self.gender==1: #Male

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandUp.png"))#0
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandRight.png"))#1
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandDown.png"))#2
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandLeft.png"))#3

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkUpRight.png"))#4
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkUpLeft.png"))#5

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkRightRight.png"))#6
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkRightLeft.png"))#7

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkDownRight.png"))#8
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkDownLeft.png"))#9

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkLeftRight.png"))#10
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkLeftLeft.png"))#11


        elif self.gender==2: #Female
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandUp.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandRight.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandDown.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandLeft.png"))

    def show(self):
        CurrentSprite=self.Sprites[self.spriteNo]
        p5.image_mode("CENTER")
        p5.image(CurrentSprite,(width/2,height/2),size=(CurrentSprite.size[0]*self.screenScale,CurrentSprite.size[1]*self.screenScale))

    def turnUp(self):
        self.spriteNo=5

    def turnRight(self):
        self.spriteNo=7

    def turnDown(self):
        self.spriteNo=9

    def turnLeft(self):
        self.spriteNo=11

    def walkingAnimation(self,Map):
        if self.walkTimer%self.walkingAnimationTime==1:
            if Map.dir==0:
                if self.Right:
                    self.spriteNo=4
                    self.Right=False
                else:
                    self.spriteNo=5
                    self.Right=True
            elif Map.dir==1:
                if self.Right:
                    self.spriteNo=6
                    self.Right=False
                else:
                    self.spriteNo=7
                    self.Right=True
            elif Map.dir==2:
                if self.Right:
                    self.spriteNo=8
                    self.Right=False
                else:
                    self.spriteNo=9
                    self.Right=True
            elif Map.dir==3:
                if self.Right:
                    self.spriteNo=10
                    self.Right=False
                else:
                    self.spriteNo=11
                    self.Right=True



        elif self.walkTimer%self.walkingAnimationTime==6:
            self.spriteNo=Map.lockedDir
