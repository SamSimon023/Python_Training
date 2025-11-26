class Customer:
    def __init__(self,Name, Age, City):
        self.Name = Name
        self.Age = Age
        self.City = City

    def LoyaltyPgm(self):
        return "Eligible" if self.Age > 25 else "Not eligible"

#create object

C1=Customer("Jim", 85, "Kolkata")
print(C1.LoyaltyPgm())

