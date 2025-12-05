nums = [12, -7, 5, -3, 9, -1, 0, 8]

left = 0
right = len(nums) - 1

while left < right:
    if nums[left] < 0:
        left += 1
    elif nums[right] >= 0:
        right -= 1
    else:
        # Swap negative from right with positive from left
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

print("Rearranged list:", nums)
