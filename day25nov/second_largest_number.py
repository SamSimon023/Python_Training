nums = [23, 89, 12, 78, 55, 42]
largest=nums[0]
sec_largest=nums[0]
for i in nums:
    if i > largest:
        sec_largest=largest
        largest=i
    elif i>sec_largest and i!=largest:
        sec_largest=i
print("Second largest number is ",sec_largest)