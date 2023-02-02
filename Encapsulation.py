class BankAccount:
    def __init__(self, balance):
        #protected variable that can't access by other class
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

Name = input("\nhey User, Enter your name : ")
balance = int(input(f"hey {Name}, Enter your current balance : "))
Name = BankAccount(balance)
UserInput = int(input("For Deposite enter 1 and for withdraw enter 2 : "))

if UserInput == 1:
    DepositeAmount = int(input("How many ruppes you want to Deposite : "))
    Name.deposit(DepositeAmount)
    NewBal = Name.get_balance
    print(f"Remaining Balance after deposite is {Name.get_balance()}\n")
else:
    WithdrawAmount = int(input("How many ruppes want to withdraw : "))
    if Name.withdraw(WithdrawAmount):
        NewBal = Name.get_balance
        print(f"Remaining balance after withdraw ia {Name.get_balance()}\n")
    else:
        print("Sorry your withdraw request is rejected!, cause Your withdraw amount is greater then balance.\n")
