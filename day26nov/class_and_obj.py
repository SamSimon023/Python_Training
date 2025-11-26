# class Student:
#     pass
#
# s1=Student() #new object being created
# s2=Student()
#
# ##################################################
#
# class Student:
#     def __init__(self,name,age,): #Constructor
#         self.name = name
#         self.age = age
#
# s3=Student("Sam",22) #object 1 created
# s4=Student("Ram",23) #object 2 in created
#
# print(s3.name, s3.age)
# print(s4.name, s4.age)
'''
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def display(self):
        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Price :",self.price)

#Creating 3 car objects
car1=Car("Toyota","Fortuner",4500000)
car2=Car("Mercedes","E-class",8500000)
car3=Car("BMW","720li",12300000)

#Displaying details
car1.display()
print()
car2.display()
print()
car3.display()'''

class Employee:
    def __init__(self,emp_id,name,department,salary):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.salary=salary
    def display(self):
        print("Employee ID :",self.emp_id)
        print("Name :",self.name)
        print("Department :",self.department)
        print("Salary :",self.salary)

#Creating objects
e1=Employee(1001,"John","HR",1200000)
e2=Employee(1002,"Michael","CT",1000000)

#Display details
e1.display()
print()
e2.display()