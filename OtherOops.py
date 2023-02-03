#This is a program of oops concept and it is for Wappnet System

from abc import ABC, abstractmethod
import constant
#Public Class
#Base Class
class person(ABC):

    #Public data member
    PCount = 0

    #abstract method
    @abstractmethod
    def hey(self):
        pass

    #private data Member
    __Confidential = 200

    #Protected data member
    _DevPeDaySal = 1000
    _DesPeDaySal = 800
    _BdePeDaySal = 900

    #Static method
    def Risky():
        print(f"Total project pending is {person.__Confidential}")


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
            _PeDaySal = person._DevPeDaySal

        elif self.pos == "designer":
            _PeDaySal = person._DesPeDaySal

        else:
            _PeDaySal = person._BdePeDaySal

        return _PeDaySal

#Protected Class
#Inherited class
class _employe(person):

    def hey(self):
        print("employe calss hey method")

    def salary(self):
        posal = super()._PosSalAssig()
        Sal = self.wday * posal

        return print(f"\tHey {self.name},your Salary is {Sal}")

#Multiple inheritance
class ceo(_employe):

    def hey(self):
        print("ceo calss hey method")

    def __init__(self, Name, EmpId, Pos, Wday):
        super().__init__(Name, EmpId, Pos, Wday)
        self.Npos = Pos

    def hey(self):
        print("hey, how are you, This is an ceo class method.")

    #public method for changing the salary.
    def Change_Sal(self,Npos):
        if Npos == "developer":
            person._DevPeDaySal = 1500
        elif Npos == "designer":
            person._DesPeDaySal = 1200
        else:
            person._BdePeDaySal = 1100

    def promotion(self):
        print(f"Hey, your new salary is {person.Change_Sal(self.Npos)}")


#public method
def main():

    global Name
    Name = input("\n\tEnter Your Name : ")
    global EmpID

    #Type Casting
    EmpID = int(input("\tEnter your Employe ID : "))
    global Pos
    Pos = input("\tEnter your Role: ")
    Pos = Pos.lower()
    global Wday
    Wday = int(input("\tEnter your working days at company : "))
    P = ceo(Name,EmpID,Pos,Wday)

    # Nested ifelse
    if Wday == 30:
        if Pos == "developer":
            P.Change_Sal(Pos)
        elif Pos == "designer":
            P.Change_Sal(Pos)
        else:
            P.Change_Sal(Pos)

    Jadu = P.salary()

    return Jadu

print(f'''
 ***** Hello user This is a {constant.COMPANY_NAME} Salary counting system. ****
        For Knowing your salary enter the below data
''')

Persons = int(input("How many users Salary you want to Know : "))

#loop for checking the salaries
for i in range(Persons):
    main()

    #Condition for verify comittie member
    Key = int(input("\nIf you are comittie member, Enter secret code : "))
    if Key == 112:
        person.Risky()
        person.PCount += 1
    else:
        print("\nIncorrect code! ")
    i += 1

#Count for How many user check the confidential data.
print(f"\nTotal persons till date checked is {person.PCount}\n")
print(f"For any query send mail to {constant.SUPPORT_EMAIL}")
print(f"Project name is {constant.PROJECT_NAME}")