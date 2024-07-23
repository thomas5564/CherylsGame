from Mm import Mm

class Tree(Mm):
    def __init__(self, posx, posy, height):
        super().__init__(posx, posy)  # Initialize the base class
        self.height = height

    def set_Height(self,large):
        self.height = large

    def get_height(self):
        return self.height
