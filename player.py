import p5

class Player:


    def __init__(self,gender,sprite,screenScale):
        
        self.gender=gender
        self.spriteNo=sprite
        self.screenScale=screenScale/6

        self.Sprites=[]
        if self.gender==1:
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandUp.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandRight.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandDown.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandLeft.png"))
        elif self.gender==2:
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandUp.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandRight.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandDown.png"))
            self.Sprites.append(p5.load_image(r"Images\Characters\TrainerFemale\FemaleTrainerStandLeft.png"))

    def show(self):
        CurrentSprite=self.Sprites[self.spriteNo]
        p5.image_mode("CENTER")
        p5.image(CurrentSprite,(width/2,height/2),size=(CurrentSprite.size[0]*self.screenScale,CurrentSprite.size[1]*self.screenScale))

