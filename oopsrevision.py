class fruit:
    def __init__(self, name, colour, shape, isFibre):
        self.name=name
        self.colour=colour
        self.shape=shape
        self.isFibre=isFibre
    def inputs(self):
        self.name=input("What is the name of the fruit?")
        self.colour=input("What colour is the fruit?")
        self.shape=input("What shape is the fruit?")
        self.isFibre=input("Does the fruit have fibre?")
    def display(self):
        print(self.name)
        print(self.colour)
        print(self.shape)
        print(self.isFibre)

fruit1=fruit("Kiwi", "Green", "Round", True)
fruit2=fruit("Strawberry", "Red", "Triangular", True)

#Calling class function
fruit1.display()
fruit2.display()
fruit1.inputs()
fruit1.display()