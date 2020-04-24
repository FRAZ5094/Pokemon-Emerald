import p5
from time import sleep
class Player:


    def __init__(self,gender,sprite,screenScale):
        
        self.gender=gender
        self.spriteNo=sprite
        Upscaled=6
        self.screenScale=screenScale/Upscaled

        self.RightFoot=True
        self.Walking=False
        self.Walkingcount=0


        self.Sprites=[]
        if self.gender==1: #Male

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandUp.png"))#1
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandRight.png"))#2
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandDown.png"))#3
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandLeft.png"))#4

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkUpRight.png"))#5
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkUpLeft.png"))#6

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkRightRight.png"))#7
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkRightLeft.png"))#8

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkDownRight.png"))#9
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkDownLeft.png"))#10

            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkLeftRight.png"))#11
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerWalkLeftLeft.png"))#12


        elif self.gender==2: #Female
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandUp.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandRight.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandDown.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandLeft.png"))

    def show(self):
        CurrentSprite=self.Sprites[self.spriteNo]
        p5.image_mode("CENTER")
        p5.image(CurrentSprite,(width/2,height/2),size=(CurrentSprite.size[0]*self.screenScale,CurrentSprite.size[1]*self.screenScale))

    def walkUpAnimation(self):
        if self.RightFoot:
            self.spriteNo=5
            sleep(self.WalkTime)
            self.spriteNo=1
            self.RightFoot=False
        else:
            self.spriteNo=6
            sleep(self.WalkTime)
            self.spriteNo=1
            self.RightFoot=True

