# Problem 239 leetcode

# nums = [1,3,-1,-3,5,3,6,7]
# k = 5

nums = [2,4,7]
k = 2

# maxSum approach
# wSum = 0
# mSum = -999999

# for i in range(0, k):
#     wSum += nums[i]

# for i in range(k, len(nums)):
#      wSum = wSum - nums[i - k] + nums[i]
#      mSum = max(wSum, mSum)
# print(mSum)

######################

# O(n**2) approach
# newArr = []
# for i in range(0, len(nums) - (k - 1)):
#     max = -99999;
#     for j in range(i, i + k):
#         if (nums[j] > max):
#             max = nums[j]
#     newArr.append(max)
# print(newArr)

######################
# Optimal Solution Pending

newArr = []
mVal = -99999999
for i in range(0, k):
    if nums[i] > mVal:
         mVal = nums[i]
newArr.append(mVal)
    
for i in range(1, len(nums) - (k - 1)):
    if nums[i - 1] == mVal:
        mVal = -99999999
    mVal = max(mVal, nums[i + k - 1])
    newArr.append(mVal)

# for i in range(1, len(nums)- (k - 1)):
#     if nums[i + k - 1] > mVal:
#         mVal = nums[i + k - 1]
#     elif nums[i - 1] == mVal:
#         mVal = -99999999
#         for j in range(i, i + k):
#             if nums[j] > mVal:
#                 mVal = nums[j]
#     newArr.append(mVal)
print(newArr)






    


    

