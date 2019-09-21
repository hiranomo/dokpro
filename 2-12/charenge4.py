class Hexagon:
    def __init__(self,h):
        self.hen = h
    def gaishu(self):
        return self.hen * 6

hexagon = Hexagon(10)
print(hexagon.gaishu())
