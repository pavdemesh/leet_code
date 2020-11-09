def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    shift = None

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            right = mid - 1

        if nums[mid] < nums[mid - 1]:
            shift = mid

    if shift is None:
        shift = left

    print("Shift is at position:", shift)

    if shift == 0:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    if target >= nums[0]:
        left = 0
        right = shift - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    else:
        left = shift
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    return -1


print(search_rotated_array([7, 0, 1, 2, 4, 5, 6], 6))
print(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 6))
print(search_rotated_array([6, 7, 0, 1, 2, 4, 5], 6))
print(search_rotated_array([0, 1, 2, 4, 5, 6, 7], 0))
