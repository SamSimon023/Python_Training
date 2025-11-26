class Student:
    def __init__(self,Name,m1,m2,m3):
        self.Name=Name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def total(self):
        return self.m1+self.m2+self.m3

    def percentage(self):
        return (self.total()/300)*100

    def display(self):
        print("Name :",self.Name)
        print("Marks :",self.m1,self.m2,self.m3)
        print("Total :",self.total(),"out of total 300!")
        print("Percentage :",self.percentage())

#create object

s1=Student("Samuel",85,89,95)

#display details
s1.display()