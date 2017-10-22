class Dot():
    def __init__(self, x, y):
        self.value = 10
        self.x = x
        self.y = y
        self.height = 33
        self.width = 10
        self.img = [pyglet.image.load("img/dot.png")]
        self.spr = pyglet.sprite.Sprite(self.img[0], x=self.x, y=self.y)
