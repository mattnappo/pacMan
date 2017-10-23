import pyglet
from pyglet.window import key
from pyglet.gl import *
from pacMan import PacMan
from dot import Dot
from barrier import Barrier
from rect import Rect
#----------------SETUP SPRITES & ANIMATION----------------
def loader(location, listName, amount):
    for i in range(amount):
        tmpImg = pyglet.image.load(location+str(i)+".png")
        runSprite = pyglet.sprite.Sprite(tmpImg, x=0, y=-0)
        listName.append(runSprite)
global pacAnimate
pacAnimate = False
global pacCycle
pacCycle = 0
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

def animatePac(dt):
    global pacCycle
    if pacAnimate == True:
        if pacCycle < 3:
            pacCycle+=1
        else:
            pacCycle = 0
#----------------SETUP GAME--------------------
window = pyglet.window.Window(457, 566)
keys = key.KeyStateHandler()
window.push_handlers(keys)
#----------------CREATE OBJECTS----------------
barriers = [
    Barrier(49, 525, 50, 67)
]

char = PacMan(0, 0, barriers)
#----------------EVENTS---------------------
@window.event
def on_draw():
    global pacCycle
    pyglet.sprite.Sprite(pyglet.image.load("img/boards/lvl1.jpg"), x=0, y=0).draw()

    if char.right == True or char.left == True or char.up == True or char.down == True:
        if char.direction == "right":
            char.spr = pacRight[pacCycle]
        elif char.direction == "left":
            char.spr = pacLeft[pacCycle]
        elif char.direction == "up":
            char.spr = pacUp[pacCycle]
        elif char.direction == "down":
            char.spr = pacDown[pacCycle]
    char.move()
    char.spr.draw()

@window.event
def on_key_press(symbol, modifiers):
    global pacAnimate
    pacAnimate = True
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
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS, ('v2f', [x, y, x-dx, y, x-dx, y-dy, x, y-dy]))
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
pyglet.clock.schedule_interval(animatePac, 1/14.0)
pyglet.app.run()
