import p5

class Player:


    def __init__(self,x,y,sprite,scale):
        self.pos=p5.Vector(x,y)
        self.spriteNo=sprite
        self.scale=scale

        self.Sprites=[]
        self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandUp.png"))
        self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandRight.png"))
        self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandDown.png"))
        self.Sprites.append(p5.load_image(r"Images\Characters\TrainerMale\MaleTrainerStandLeft.png"))

    def show(self):
        CurrentSprite=self.Sprites[self.spriteNo]
        p5.image_mode("CENTER")
        p5.image(CurrentSprite,(width/2,height/2),size=(CurrentSprite.size[0]*self.scale,CurrentSprite.size[1]*self.scale))


    def moveUp():
        pass
