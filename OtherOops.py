#This is a program of oops concept and it is for Wappnet System 

#Public Class 
#Base Class
class person():

    #Public data member
    PCount = 0

    #Private data member
    __DevPeDaySal = 1000
    __DesPeDaySal = 800
    __BdePeDaySal = 900

    #constructor
    #Public Method
    def __init__(self,Name,EmpId,Pos,Wday):
        self.name = Name
        self.empid = EmpId
        self.pos = Pos
        self.wday = Wday

    #Method for checking the daily salary of employes
    #Protected method
    def _PosSalAssig(self):
        _PeDaySal = 0
        if self.pos == "developer":
            #Protected object
            _PeDaySal = person.__DevPeDaySal

        elif self.pos == "designer":
            _PeDaySal = person.__DesPeDaySal
        
        else:
            _PeDaySal = person.__BdePeDaySal

        return _PeDaySal

#Protected Class
#Inherited class
class _employe(person):


    def salary(self):
        psal = person(Name,EmpID,Pos,Wday)
        posal = psal._PosSalAssig()
        Sal = self.wday * posal

        return print(f"\tHey {self.name},your Salary is {Sal}")

#public method
def main():

    global Name
    Name = input("\n\tEnter Your Name : ")
    #Type Casting
    global EmpID
    EmpID = int(input("\tEnter your Employe ID : "))
    global Pos
    Pos = input("\tEnter your Role: ")
    Pos = Pos.lower()
    global Wday
    Wday = int(input("\tEnter your working days at company : "))
    P = _employe(Name,EmpID,Pos,Wday)
    Jadu = P.salary()
    return Jadu

print('''

 ***** Hello user This is a Wappnet Salary counting system. ****

        For Knowing your salary enter the below data

''')

Persons = int(input("How many users Salary you want to Know : "))
for i in range(Persons):
    main()
    person.PCount += 1
    i += 1

print(f"\nTotal persons till date checked is {person.PCount}\n")