value=int(input("Enter number of times to rotate : "))
list=[6,7,8,9,10,1,2,3,4,5]
list.append(6)
j=0
while j<value:
    for i in range(0,len(list)):
        list[i],list[i-1]=list[i-1],list[i]
    print(list)
    j+=1
list.pop()
print(list)