n=int(input("Enter number : "))
s=0
r=0
while n!=0:
    r=n%10
    s=s*10+r
    n//=10
print("Reverse is : ",s)