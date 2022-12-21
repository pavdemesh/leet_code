def removeDuplicates(nums):
    if not nums:
        return 0
    
    # variable to iterate over the 
    i = 0
    
    # length of the array
    N = len(nums)
    
    # cursor to keep track from where to insert
    insert_from = 0
    
    # variable to keep track of valid length of the array
    valid_length = 1
    
    # iterate over the array
    while i < (N - 1) and insert_from < N:
        # if previous less than next = everything is fine, non-decreasing order, just move by 1
        # increase valid length by 1
        if nums[i] < nums[i + 1]:
            i += 1
            valid_length += 1
            insert_from += 1
        # if not - check whether current inserton candidate is not equal to current {index]
        # if not equal - insert candidate and move insertion search index by 1, increae valid_length by 1
        elif nums[i] != nums[insert_from]:
            nums[i + 1] = nums[insert_from]
            insert_from += 1
            i += 1
            valid_length += 1
        # if move insertion candidate search by 1
        else:
            insert_from += 1
    
    #return valid length
    return valid_length
		

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))