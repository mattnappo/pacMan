import pyglet
class PacMan():
    def __init__(self, x, y, barriers):
        self.collide = 0
        self.x = x
        self.y = y
        self.height = 30
        self.width = 30
        self.img = pyglet.image.load("img/spr/pacMan/up/0.png")
        self.spr = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
        self.vel = 10
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.direction = ""
        self.barriers = barriers
    def stop(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
    def detect(self):
        if self.x + self.width >= 467:
            self.x = 467 - self.width
            self.spr.x = self.x
        elif self.x <= 0:
            self.x = 0
            self.spr.x = self.x
        for barrier in self.barriers:
            if self.x < barrier.x + barrier.width and self.x + self.width > barrier.x and self.y < barrier.y + barrier.height and self.height + self.y > barrier.y:
                self.collide += 1
                print("collide")
                return True
        return False
        '''
        # print(str(self.collide), str(self.direction))
        if barrier.x + barrier.width > self.x: # right
            # self.x = barrier.x + barrier.width
            print("right collide")
        if self.x + self.width > barrier.x: # left
            # self.x = barrier.x - self.width
            print("left collide")
        if self.y + self.height > barrier.y: # bossom
            # self.y = barrier.y - self.height
            print("bottom collide")
        if barrier.y + barrier.height > self.y: # top
            # self.y = barrier.y + barrier.height
            print("top collide")

        self.spr.x = self.x
        self.spr.y = self.y
        '''
    def move(self):
        if self.detect() == False:
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
            if self.detect == True:
                oldDirection = self.direction
                self.up = False
                self.down = False
                self.left = False
                self.right = False
                if self.direction != oldDirection:
                    self.detect = False
                self.spr.x = self.x
                self.spr.y = self.y
