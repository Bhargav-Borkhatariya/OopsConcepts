class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.x * self.y

class Square(Shape):
    def __init__(self, x):
        super().__init__(x, x)

    def area(self):
        return self.x * self.y

def calculate_area(shape):
    return shape.area()

Name = input("\nhey user, Enter your name : ")
UserInput = int(input(f"hey {Name}, For rectangle area type 1 and for square type 2 : "))
if UserInput == 1:
    hieght,wieght = input("Enter height space and then width  : ").split( )
    rect = Rectangle(int(hieght),int(wieght))
    print("Area:", calculate_area(rect),"\n")
elif UserInput == 2:
    Radius = int(input("Enter the radius of the square : "))
    sq = Square(Radius)
    print("Area:", calculate_area(sq),"\n")
else:
    print("You should type 1 or 2.\n")