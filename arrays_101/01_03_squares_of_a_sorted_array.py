# https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3240/

"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation: After squaring, the array becomes [16 ,1, 0, 9, 100].
After sorting, it becomes [0, 1, 9, 16, 100].

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

!!! Squaring each element and sorting the new array is very trivial
!!! could you find an O(n) solution using a different approach?
"""

# My solution idea is based on the fact that (-4) ** 2 == 4 ** 2, which means that:
# (-4) ** 2 will take the same place in sorted squared array as (4)  would in the original array.
# Solution steps are:
# 1) split the original array into negative (<0) and non-negative(>0) part
# 2) change sign of elements in the negative array and reverse its order: [-7, -4, - 2] becomes [2, 4, 7]
# These two "halves" of the original array are now both sorted in non-decreasing order
# 3) merge these two arrays preserving sorted order, O(n) operations needed
# 4) square each number of the resulting sorted array

# Other good solution ideas:
# https://nycdatascience.com/blog/student-works/squaring-a-sorted-array-in-python/
# https://kodebinary.com/sort-squares-of-a-sorted-array-in-linear-runtime-on/
# https://coding-gym.org/challenges/squares-of-a-sorted-array/


def sorted_squares(nums):
    # Two fast checks:
    # If first element >= 0, array consist only non-negative and will preserve its order when squared
    if nums[0] >= 0:
        return [x ** 2 for x in nums]
    # If last element < 0, array consists of only negative ints and must be reversed and squared
    if nums[-1] < 0:
        return [x ** 2 for x in nums[::-1]]

    # Else the array contains at least one negative int
    # Create empty lists to store negative and positive elements from original array
    negatives = list()
    positives = list()

    # Iterate over the original array by index and append negative ints to negatives, stop on first 0 or positive int
    split_point = 0
    while nums[split_point] < 0:
        negatives.append(nums[split_point])
        split_point += 1

    # Append the rest to positives list
    positives[:] = nums[split_point:]

    # Reverse the list of negatives and make its elements positive:
    negatives = [-x for x in negatives[::-1]]

    # Merge the negatives and positives lists preserving their sorted order
    sorted_by_abs = list()

    # Create counters to keep track of current index in each list
    i = 0
    j = 0
    # Iterate over both lists and compare element by element
    # Append smaller element to resulting array and increase index counter for source array
    while i < len(negatives) and j < len(positives):
        if negatives[i] <= positives[j]:
            sorted_by_abs.append(negatives[i])
            i += 1
        else:
            sorted_by_abs.append(positives[j])
            j += 1

    # After one of the arrays ended, append remaining elements from the other array
    if i < len(negatives):
        sorted_by_abs.extend(negatives[i:])
    else:
        sorted_by_abs.extend(positives[j:])

    # return resulting list with every element squared
    return [x ** 2 for x in sorted_by_abs]


test_arr = [-7, -4, -1, 0, 3, 10]
print(sorted_squares(test_arr))
