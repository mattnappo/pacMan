import pyglet
from pyglet.window import key

class Board():
    def __init__(self):
        self.height = 556
        self.width = 447
        self.img = pyglet.image.load("img/boards/lvl1.jpg")
        self.board = pyglet.sprite.Sprite(self.img, x=0, y=0)
class Dot():
    def __init__(self, x, y):
        self.value = 10
        self.x = x
        self.y = y
        self.height = 33
        self.width = 10
        self.img = [pyglet.image.load("img/dot.png")]
        self.spr = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
class Wall():
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
class PacMan():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = 0

        self.vel = 5

        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.lastDir = ""

        self.width = 30
        self.height = 30
        self.img = pyglet.image.load("img/spr/pacMan/right/0.png")
        self.character = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)
    def move(self):
        global pacAnimate
        #DETECTION
        for i in range(len(walls)):
            if self.x >= walls[i].x and self.x <= walls[i].x + walls[i].length:
                if self.y <= walls[i].y and self.y >= walls[i].y:
                    self.y = walls[i].y
                    self.character.y = self.y
        #no movement
        if self.left == False and self.right == False and self.up == False and self.down == False:
            if self.lastDir == "left":
                self.left = True
                self.right = False
                self.up = False
                self.down = False
            elif self.lastDir == "right":
                self.left = False
                self.right = True
                self.up = False
                self.down = False
            elif self.lastDir == "up":
                self.left = False
                self.right = False
                self.up = True
                self.down = False
            elif self.lastDir == "down":
                self.left = False
                self.right = False
                self.up = False
                self.down = True

        #up
        if self.up == True:
            self.y = self.y + self.vel
            self.character.y = self.y
            self.lastDir = "up"
        #down
        if self.down == True:
            self.y = self.y - self.vel
            self.character.y = self.y
            self.lastDir = "down"
        #left
        if self.left == True:
            self.x = self.x - self.vel
            self.character.x = self.x
            self.lastDir = "left"
        #right
        if self.right == True:
            self.x = self.x + self.vel
            self.character.x = self.x
            self.lastDir = "right"
    def dotDetect(self):
        for i in range(len(dots)):
            if self.x + self.width >= dots[i].x and self.x <= dots[i].x + dots[i].width:
                if self.y + self.height - 5 >= dots[i].y and self.y <= dots[i].y + dots[i].height -5:
                    self.points+=10
                    dots.remove(dots[i])
    def offBoard(self): #left and right detection
        if self.x <= 0:
            self.x = 0
            self.character.x = self.x
        elif self.x + self.width >= board.width:
            print()
            self.x = 447
            self.character.x = self.x

global pacAnimate
pacAnimate = False
global ghostAnimate
ghostAnimate = True
global pacCycle
pacCycle = 0
global ghostIndex
ghostIndex = 0
global caller
caller = False
global pacUp
pacUp = []
global pacDown
pacDown=[]
global pacLeft
pacLeft = []
global pacRight
pacRight = []

def loader(location, listName, amount):
    for i in range(amount):
        tmpImg = pyglet.image.load(location+str(i)+".png")
        runSprite = pyglet.sprite.Sprite(tmpImg, x=0, y=-0)
        listName.append(runSprite)
loader("img/spr/pacMan/left/", pacLeft, 4)
loader("img/spr/pacMan/right/", pacRight, 4)
loader("img/spr/pacMan/up/", pacUp, 4)
loader("img/spr/pacMan/down/", pacDown, 4)
def animatePac(dt):
    global pacCycle
    if pacAnimate == True:
        if pacCycle < 3:
            pacCycle+=1
        else:
            pacCycle = 0
def animateGhosts(dt):# GHOST EVERYTHINGS ARE GOING TO NEED TO BE FOR LOOPED == MULTIPLE GHOSTS
    global ghostIndex
    if ghostAnimate == True:
        if ghostIndex < 3:
            ghostIndex+=1
        else:
            ghostIndex = 0

global dots
dots = [ # THIS IS GONNA BE A PAIN IN THE ASS (unless I can be smart and automatic it)
            Dot(160, 237),
            Dot(75, 75),
            Dot(100, 100)
            # ...
        ]
global walls
walls = [
        Wall(467, 299, 450, 15), # center
        Wall(0, 299, 190, 15), # left
        Wall(1175, 299, 185, 15), # right
        Wall(0, 179, 1440, 15), # ground
        Wall(910, 433, 255, 15), #  upper right
        Wall(200, 433, 260, 15), # upper left
        Wall(447, 588, 470, 15) # upper center
]
board = Board()
window = pyglet.window.Window(457, 566)
window.set_caption("PacMan?")

global char
char = PacMan(45, 175)

keys = key.KeyStateHandler()
window.push_handlers(keys)

@window.event
def on_draw():
    global pacCycle
    global ghostIndex
    global walls
    global coinIndex
    window.clear()
    board.board.draw()
    if char.right == True or char.left == True:
        if char.lastDir == "left":
            char.character = pacLeft[pacCycle]
        elif char.lastDir == "right":
            char.character = pacRight[pacCycle]
        elif char.lastDir == "up":
            char.character = pacUp[pacCycle]
        elif char.lastDir == "down":
            char.character = pacDown[pacCycle]
    if len(dots) <= 0:
        board.board = pyglet.sprite.Sprite(pyglet.image.load("img/boards/lvl2.jpg"), x=0, y=0)
        # make the new dots
    # enemy.move()
    # enemy.character.draw()
    char.move()
    print("x: " + str(char.character.x))
    print("y: " + str(char.character.y))
    char.character.draw()
    points = pyglet.text.Label("Points: " + str(char.points), font_name='Times New Roman', font_size=36, x=20, y=20)
    points.draw()
    for i in range(len(dots)):
        dots[i].spr.draw()

@window.event
def on_key_press(symbol, modifiers):
    global pacAnimate
    pacAnimate = True
    if symbol == key.A:
        char.left = True
        char.right = False
        char.up = False
        char.down = False
    elif symbol == key.D:
        char.left = False
        char.right = True
        char.up = False
        char.down = False
    elif symbol == key.S:
        char.left = False
        char.right = False
        char.up = False
        char.down = True
    elif symbol == key.W:
        char.left = False
        char.right = False
        char.up = True
        char.down = False
@window.event
def on_key_release(symbol, modifiers):
    global pacAnimate
    if symbol == key.A:
        char.left = False
    elif symbol == key.D:
        char.right = False
    elif symbol == key.W:
        char.up = False
    elif symbol == key.S:
        char.down = False
def deClogger(dt):
    char.offBoard()
    char.dotDetect()
    # enemy.wallDetector()
    # changeEnemyLocation()

pyglet.clock.schedule_interval(deClogger, 1/60.0)
pyglet.clock.schedule_interval(animatePac, 1/8)
pyglet.app.run()
