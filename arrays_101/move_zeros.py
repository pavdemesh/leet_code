def moveZeroes(nums):
  """
  Do not return anything, modify nums in-place instead.
  """
 
  insert_index = 0

  for j in range(len(nums)):
    if nums[j] != 0:
      nums[insert_index], nums[j] = nums[j], nums[insert_index]
      insert_index += 1
  return nums


print(moveZeroes([5,6,7,0,0,0,1,0,3,12]))
