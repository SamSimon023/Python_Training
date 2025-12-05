nums=[0, 3, 0, 5, 7, 0, 9]
count=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[count]=nums[i]
        count+=1
while count<len(nums):
    nums[count]=0
    count+=1

print(nums)