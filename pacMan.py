import pyglet
class PacMan():
    def __init__(self, x, y, barriers):
        self.x = x
        self.y = y
        self.height = 30
        self.width = 30
        self.img = pyglet.image.load("img/spr/pacMan/up/0.png")
        self.spr = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
        self.vel = 9
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.direction = ""
        self.barriers = barriers
    def detect(self):
        if self.x + self.width + 2 >= 457:
            self.x = 457 - self.width - 4
            self.spr.x = self.x
        elif self.x + 4 <= 0:
            self.x = 0
            self.spr.x = self.x
        for barrier in self.barriers:
            if self.x + self.width >= barrier.x and barrier.x + barrier.width <= self.x:
                if self.y <= barrier.y + barrier.height and self.y + self.height >= barrier.y:
                    print("DETECTED")
    def move(self):
        self.detect()
        # CONTINUE MOVING WHEN NO KEYPRESS
        if self.right == False and self.left == False and self.up == False and self.down == False:
            if self.direction == "up":
                self.up = True
                self.down = False
                self.left = False
                self.right = False
            elif self.direction == "down":
                self.up = False
                self.down = True
                self.left = False
                self.right = False
            elif self.direction == "left":
                self.up = False
                self.down = False
                self.left = True
                self.right = False
            elif self.direction == "right":
                self.up = False
                self.down = False
                self.left = False
                self.right = True
        # MOVE
        else:
            if self.up == True:
                self.y = self.y + self.vel
                self.spr.y = self.y
                self.spr.x = self.x
            elif self.down == True:
                self.y = self.y - self.vel
                self.spr.y = self.y
                self.spr.x = self.x
            elif self.left == True:
                self.x = self.x - self.vel
                self.spr.x = self.x
                self.spr.y = self.y
            elif self.right == True:
                self.x = self.x + self.vel
                self.spr.x = self.x
                self.spr.y = self.y
