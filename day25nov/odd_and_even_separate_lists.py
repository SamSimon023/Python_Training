nums = [10, 3, 5, 12, 8, 7, 1]
odd=[]
even=[]
for i in nums:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Numbers :",even)
print("Odd Numbers :",odd)