def bSearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2) 
        elem = nums[mid]
        
        if elem == target:
            return mid
        elif elem < target:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1

print(bSearch([-1,0,3,5,9,12], 10))
