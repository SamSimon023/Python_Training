#Single Inheritance Eg1
'''
class Vehicle:
    def __init__(self,make,model,year,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage

class Car(Vehicle):
    def __init__(self,make,model,year,mileage,company,price):
        super().__init__(make,model,year,mileage)
        self.company=company
        self.price=price

c=Car("Teflon","T4F5",2020,23,"BMW",12000000)
print("Make - ",c.make,"Model - ",c.model,"Year - ",c.year,"Mileage - ",c.mileage,"Company - ",c.company,"Price - ",c.price)
'''

#Eg2

class Product:
    def __init__(self,product_id,name,quantity,rating):
        self.product_id=product_id
        self.name=name
        self.quantity=quantity
        self.rating=rating

    def display_items(self):
        print(self.product_id,self.name,self.quantity,self.rating)

class Electronics(Product):
    def __init__(self,product_id,name,quantity,rating,warranty_period,power_consumption,model_number):
        super().__init__(product_id,name,quantity,rating)
        self.warranty_period=warranty_period
        self.power_consumption=power_consumption
        self.model_number=model_number

    def display_items(self):
        print(self.product_id,self.name,self.quantity,self.rating)

e=Electronics("##1234","Phone",1234,5,"5 years","2000W",10209836)
print(e.display_items())