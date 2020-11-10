# Solution from errichto

def min_rotated_array(nums):
    """Returns index of the smallest element in rotated sorted list"""
    n = len(nums)
    left, right = 0, len(nums) - 1
    ans = None

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] <= nums[n - 1]:

            ans = mid

            right = mid - 1  # look for something even smaller on the left

        else:
            left = mid + 1

    return ans


print(min_rotated_array([2, 6, 7, 9, 0, 1]))
