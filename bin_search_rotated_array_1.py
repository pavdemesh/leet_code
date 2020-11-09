# Search in Rotated Sorted Array, https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
# This is the harder of two rotated-array problems in Leetcode.

# There are two options:
# 1) First find the rotation (the position of the smallest element)
# and then find the target value in one of the parts.
# This approach requires one binary search and then another different binary search.
# 2) Run one binary search with more complicated if-conditions to look for the number:
# this is what my code does. You should try yourself the first approach.

def search_shifted_array(nums: List[int], target: int) -> int:
    # For each number we can check if we should go to the left/right
    # by comparing it with target and with a[0].
    # Also, comparing target with a[0] tells us in which part (big or small numbers) the target is.

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid  # no need to store the answer, just return it

        if target >= nums[0] and (nums[mid] >= target or nums[mid] < nums[0]):
            right = mid - 1

        elif target < nums[0] and (nums[0] > nums[mid] >= target):
            right = mid - 1

        else:
            left = mid + 1
    return -1
