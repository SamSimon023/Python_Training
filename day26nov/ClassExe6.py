class Product:
    def __init__(self,Name,Price,Quantity):
        self.Name=Name
        self.Price=Price
        self.Quantity=Quantity

    def Total(self):
        return self.Price*self.Quantity

    def display(self):
        print("Product Name:",self.Name)
        print("Price:",self.Price)
        print("Quantity:",self.Quantity)

#create object
p1=Product("Milk",50,5)

p1.display()
print("Total Amount: ",p1.Total())