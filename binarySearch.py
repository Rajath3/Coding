# Iterative approach
def binarySearch(nums, target):
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

# print(binarySearch([-1,0,3,5,9,12], 10))


# Recursive approach

def bSearch(nums, target, low, high):
    if low > high:
        print('Not Found')
        return
    
    mid = int((low + high)/2)
    if nums[mid] == target:
        print("Index," + str(mid)) 
        return
    
    elif nums[mid] < target:
        return bSearch(nums, target, mid + 1, high)
    else:
        return bSearch(nums, target, low, mid - 1)

nums = [-9, -1,0,3,5,9,12]
print(bSearch(nums, -9, low = 0, high = len(nums)))