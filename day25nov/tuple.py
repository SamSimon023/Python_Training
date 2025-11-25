'''data=10,20,30

a,b,c=data
print(a,b,c)

employee=("John",32,("Banglore","India"))
print(employee[2][0])'''

numbers=(33,20,30,60,50)
max=numbers[0]
min=numbers[0]
for i in numbers:
    if i>max:
        max=i
    elif i<min:
        min=i
print("Max is ",max,"and min is ",min)