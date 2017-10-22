import pyglet
from pyglet.window import key

class Character():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pyglet.image.load("img/spr/pacMan/up/0.png")
        self.spr = pyglet.sprite.Sprite(self.img, x=self.x, y=self.y)

        self.vel = 9

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.direction = ""

    def move(self):
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

def loader(location, listName, amount):
    for i in range(amount):
        tmpImg = pyglet.image.load(location+str(i)+".png")
        runSprite = pyglet.sprite.Sprite(tmpImg, x=0, y=-0)
        listName.append(runSprite)

global isAnimating
isAnimating = False

global cycle
cycle = 0

global pacUp
pacUp = []

global pacDown
pacDown=[]

global pacLeft
pacLeft = []

global pacRight
pacRight = []

loader("img/spr/pacMan/up/", pacUp, 4)
loader("img/spr/pacMan/down/", pacDown, 4)
loader("img/spr/pacMan/left/", pacLeft, 4)
loader("img/spr/pacMan/right/", pacRight, 4)
print(pacUp)

def animate(dt):
    global cycle
    if isAnimating == True:
        if cycle < 3:
            cycle+=1
        else:
            cycle = 0

window = pyglet.window.Window(457, 566)

keys = key.KeyStateHandler()
window.push_handlers(keys)

char = Character(0, 0)

@window.event
def on_draw():
    global cycle
    pyglet.sprite.Sprite(pyglet.image.load("img/boards/lvl1.jpg"), x=0, y=0).draw()

    if char.right == True or char.left == True or char.up == True or char.down == True:
        if char.direction == "right":
            char.spr = pacRight[cycle]
        elif char.direction == "left":
            char.spr = pacLeft[cycle]
        elif char.direction == "up":
            char.spr = pacUp[cycle]
        elif char.direction == "down":
            char.spr = pacDown[cycle]
    char.move()
    char.spr.draw()


@window.event
def on_key_press(symbol, modifiers):
    global isAnimating
    isAnimating = True
    if symbol == key.A:
        char.left = True
        char.right = False
        char.up = False
        char.down = False
        char.direction = "left"
    if symbol == key.D:
        char.right = True
        char.left = False
        char.up = False
        char.down = False
        char.direction = "right"
    if symbol == key.W:
        char.up = True
        char.down = False
        char.left = False
        char.right = False
        char.direction = "up"
    if symbol == key.S:
        char.down = True
        char.left = False
        char.right = False
        char.up = False
        char.direction = "down"

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.A:
        char.left = False
    elif symbol == key.D:
        char.right = False
    elif symbol == key.W:
        char.up = False
    elif symbol == key.S:
        char.down = False
# def deClogger(dt):


# pyglet.clock.schedule_interval(deClogger, 1/60.0)
pyglet.clock.schedule_interval(animate, 1/14.0)
pyglet.app.run()
