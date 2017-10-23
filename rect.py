import pyglet
from pyglet.gl import *

class Rect():
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2, 2,3,0],
            ("v3f",
                [
                    -0.5,-0.5,0.0,
                    0.5,-0.5,0.0,
                    0.5,0.5,0.0,
                    -0.5,0.5,0.0
                ]
            )
        )
rect = Rect()
rect.vertices.draw(GL_TRIANGLES)
