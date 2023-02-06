from multipledispatch import dispatch

class MethodOverloading():

    @dispatch(int, int)
    def jadu(self, oprand1, oprand2):
        self.oprand1 = oprand1
        self.oprand2 = oprand2
        c = self.oprand1 + self.oprand2
        return print(c)
    
    @dispatch(int, int, int)
    def jadu(self, oprand1, oprand2, oprand3):
        self.oprand4 = oprand1
        self.oprand5 = oprand2
        self.oprand6 = oprand3
        c = self.oprand4 + self.oprand5 + self.oprand6
        return print(c)

a, b, c = input("Enter the 3 values seprated by space : ").split(' ')

add = MethodOverloading()
add.jadu(int(a), int(b), int(c))
add.jadu(int(a), int(b))