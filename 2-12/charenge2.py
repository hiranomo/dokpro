import math

class Circle:
    def __init__(self,r):
        self.hankei = r
    def area(self):
        return math.pi * self.hankei ** 2

circle = Circle(10)
print(circle.area())
