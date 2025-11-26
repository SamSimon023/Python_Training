class Calculator:
    def __init__(self,Value1,Value2):
        self.value1=Value1
        self.value2=Value2

    def add(self):
        self.output=self.value1+self.value2
        print(self.output)

    def sub(self):
        self.output=self.value1-self.value2
        print(self.output)

    def multiply(self):
        self.output=self.value1*self.value2
        print(self.output)

    def divide(self):
        try:
            self.output = self.value1 / self.value2
            print(self.output)
        except:
            print("Division by zero not allowed")


    def display(self):
        print("Integer 1 - ",self.value1)
        print("Integer 2 - ",self.value2)

#add
value=Calculator(int(input("Enter integer 1: ")),int(input("Enter integer 2: ")))
value.display()
Operation=input("Enter operation: ")
if Operation=="add":
    value.add()
elif Operation=="sub":
    value.sub()
elif Operation=="multiply":
    value.multiply()
else:
    value.divide()
