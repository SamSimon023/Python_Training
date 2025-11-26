class BankAccount:
    def __init__(self,deposit,withdrawal):
        self.deposit = deposit
        self.withdrawal = withdrawal

    def balance(self):
        return self.deposit - self.withdrawal

    def transactions(self,log):
        log.append([self.deposit,self.withdrawal,self.balance()])
        return log

#create object

count=int(input("Enter number of transactions :"))
log=[]
for i in range(count):
    print("Transaction",i+1)
    b1=BankAccount(int(input("Deposit :")),int(input("Withdrawal :")))
    b1.balance()
    log=b1.transactions(log)
    print("Transaction Log[deposit,withdrawal,balance]: ",log)
