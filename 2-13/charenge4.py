class Horse:
    def __init__(self,name,rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self,name):
        self.name = name

jojo = Rider('jojo')
siro = Horse('siro',jojo)
print(siro.rider.name)
