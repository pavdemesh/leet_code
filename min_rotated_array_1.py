def min_rotated_array(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            right = mid - 1

        if nums[mid] < nums[mid - 1]:
            return mid

    return left


print(min_rotated_array([7, 0, 1, 2, 4, 5, 6]))
print(min_rotated_array([4, 5, 6, 7, 0, 1, 2]))
print(min_rotated_array([6, 7, 0, 1, 2, 4, 5]))
