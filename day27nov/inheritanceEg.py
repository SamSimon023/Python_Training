'''class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d=Dog()
d.speak()   #inherited
d.bark()    #child's own method'''

class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name)
        self.emp_id=emp_id

e=Employee("Emil",1001)
print(e.name,e.emp_id)