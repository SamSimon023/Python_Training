nums = [5, 2, 7, 5, 9, 5, 3]
n=int(input("Enter value : "))
indices=[]
for i in range(len(nums)):
    if nums[i]==n:
        indices.append(i)
print(indices)