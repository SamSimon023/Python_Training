#Multilevel inheritance Eg1

'''class Animal:
    def __init__(self,life_span,danger_level):
        self.life_span=life_span
        self.danger_level=danger_level


class Mammal(Animal):
    def __init__(self,life_span,danger_level,land_or_sea,diet):
        super().__init__(life_span,danger_level)
        self.land_or_sea=land_or_sea
        self.diet=diet

class Dog(Mammal):
    def __init__(self,life_span,danger_level,land_or_sea,diet,breed,weight):
        super().__init__(land_or_sea,diet,life_span,danger_level)
        self.weight=weight
        self.breed=breed

a1=Dog("7 years","Friendly","land","omni","German","35kg")
print("A dog attributes are - \n\t",a1.life_span,"\n\t",a1.danger_level,"\n\t",a1.breed,"\n\t",a1.weight,"\n\t",a1.land_or_sea)
'''

#Eg 2

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Employee(Person):
    def __init__(self,emp_id,department,name,age):
        super().__init__(name,age)
        self.emp_id=emp_id
        self.department=department

class Manager(Employee):
    def __init__(self,Rank,experience,emp_id,department,name,age):
        super().__init__(emp_id,department,name,age)
        self.Rank=Rank
        self.experience=experience

m1=Manager(2,"23 years",10200,"HR","Saul",54)
print("Manager details - \n\t",m1.Rank,"\n\t",m1.experience,"\n\t",m1.name,"\n\t",m1.age,"\n\t",m1.emp_id,"\n\t",m1.department)

