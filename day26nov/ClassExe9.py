class Mobile:
    def __init__(self,Brand,Model,Storage):
        self.Brand=Brand
        self.Model=Model
        self.Storage=Storage

    def Upgrade(self):
        while True:
            a = input("Do you want upgrade in storage[Y/N]: ")
            if a=="Y":
                self.Storage=self.Storage*2
                print("New storage: ",self.Storage)
            else:
                print("Final Storage: ",self.Storage)
                break

M1=Mobile("Samsung","Galaxy",64)
M1.Upgrade()