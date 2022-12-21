"""
Given an integer array nums, 
move all the even integers at the beginning of the array 
followed by all the odd integers.
Return any array that satisfies this condition.
"""

def sortArrayByParity(nums):
    insert_point = 0
    
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            nums[insert_point], nums[i] = nums[i], nums[insert_point]
            insert_point += 1
    return nums


print(sortArrayByParity([3,1,2,4]))
