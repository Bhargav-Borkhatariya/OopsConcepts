class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def addition(self):
        sum = self.a + self.b
        print("Sum is : ", sum,"\n")
    
    def double(self):
        mul = self.a * self.b
        print("Mul is ", mul,"\n")

class bank(Calculator):
    def __init__(self, a, b):
        super().__init__(a, b) 
    def deposit(self):
        super().addition()
    def pachisDivas():
        super().double()

Name = input("\nhey user, Enter your name : ")
UserInput = int(input(f"hey {Name}, For addition type 1 and for multiply type 2 : "))

if UserInput == 1:
    valA, valB = input(f"hey {Name}, Enter value for A and B : ").split()
    Name = bank(int(valA),int(valB))
    Name.addition()
    
elif UserInput == 2:
    valA, valB = input(f"hey {Name}, Enter value for A and B : ").split()
    Name = bank(int(valA),int(valB))
    Name.pachisDivas()
else:
    print("You should type 1 or 2.\n")