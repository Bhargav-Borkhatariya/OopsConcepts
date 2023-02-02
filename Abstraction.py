from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


Name = input("\nhey user, Enter your name : ")
UserInput = int(input(f"hey {Name}, For rectangle area type 1 and for circle type 2 : "))
if UserInput == 1:
    hieght,wieght = input("Enter height space and then width  : ").split( )
    rect = Rectangle(int(hieght),int(wieght))
    print("Area:", rect.area(),"\n")
elif UserInput == 2:
    Radius = int(input("Enter the radius of the square : "))
    sq = Circle(Radius)
    print("Area:", sq.area(),"\n")
else:
    print("You should type 1 or 2.\n")