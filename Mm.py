class Mm:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def getx(self):
        return self.posx

    def gety(self):
        return self.posy
    
    def move(self):
        self.posx-=10
