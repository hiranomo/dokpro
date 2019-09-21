class Shape:
    def what_am_i(self):
        print('I am a shape')

class Square(Shape):
    def __init__(self,len):
        self.len = len
    def calculate_perimeter(self):
        return self.len * 4

class Rectangle(Shape):
    def __init__(self,width,len):
        self.width = width
        self.len = len
    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2
    def change_size(self,width,len):
        self.width += width
        self.len += len

square = Square(10)
print(square.calculate_perimeter())
square.what_am_i()

rectangle = Rectangle(10,10)
rectangle.change_size(1,-2)
print(rectangle.calculate_perimeter())
rectangle.what_am_i()
