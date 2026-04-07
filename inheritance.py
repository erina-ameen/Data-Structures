class fruit:
    def __init__(self, type, shape, colour):
        self.type=type
        self.shape=shape
        self.colour=colour
        
    def inputs(self):
        self.type=input("What type of fruit is it?")
        self.shape=input("What shape is it?")
        self.colour=input("What colour is it?")

    def printing(self):
        print(self.type)
        print(self.shape)
        print(self.colour)

class inheritFruit(fruit):
    def __init__(self, type, shape, colour, citrus, stalk):
        fruit.__init__(self, type, shape, colour)
        self.citrus=citrus
        self.stalk=stalk

    #function overriding 
    def printing(self):
        print(self.type)
        print(self.shape)
        print(self.colour)
        print(self.citrus)
        print(self.stalk)

#object creation
fruit1=inheritFruit("Strawberry", "Triangular", "Red", False, True)
fruit2=inheritFruit("Orange", "Circular", "Orange", True, False)
fruit2.inputs()
fruit2.printing()