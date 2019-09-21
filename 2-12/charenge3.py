class Triangle:
    def __init__(self,th,t):
        self.teihen = th
        self.takasa = t
    def area(self):
        return self.teihen * self.takasa / 2

triangle = Triangle(2,2)
print (triangle.area())
