class BankAccount:
    def __init__(self,Customer_Name,Account_Number,Balance):
        self.Customer_Name = Customer_Name
        self.Account_Number = Account_Number
        self.Balance = Balance

    def display(self):
        print("Customer Name:",self.Customer_Name)
        print("Account Number:",self.Account_Number)
        print("Balance:",self.Balance)

    def deposit(self,amount):
        self.Balance += amount

    def withdraw(self,amount):
        self.Balance -= amount

#creating objects
a1=BankAccount("Mavrick",100120033456,50000)

#depositing money
a1.deposit(int(input("Enter amount to deposit:")))
a1.display()
print()

#withdrawing money
a1.withdraw(int(input("Enter amount to withdraw:")))
a1.display()
