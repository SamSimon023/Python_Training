nums = [10, 11, 12, 13, 17, 20, 23]
prime=[]
for num in nums:
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
    if flag==0:
        prime.append(num)
print(prime)



