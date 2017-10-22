class Guy():
    def __init__(self, color):
        self.color = color
    def printer(self):
        print(self.color)
    def runner(self):
        printer()

guy = Guy("Orange")
guy.runner()
