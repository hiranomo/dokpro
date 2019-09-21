class Square:
    def __init__(self,len):
        self.l = len
    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.l,self.l,self.l,self.l)

print(Square(30))
