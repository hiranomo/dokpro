class Square:
    square_list = []
    def __init__(self):
        self.square_list.append(self)

s = Square()
sq = Square()

print(Square.square_list)
