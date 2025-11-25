n=int(input("Enter number : "))
c=0
while n!=0:
    n=n//10
    c+=1
print("Total digits= ",c)