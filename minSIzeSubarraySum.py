# nums = [2,3,1,2,4,3]
# target = 15

# nums = [12,28,83,4,25,26,25,2,25,25,25,12]
# target = 213

target = 6
nums = [1,1,1,1,1,1,1,1]

# target = 4
# nums = [1,4,4]

length = len(nums)
low = 0
high = length - 1

i = 0
sum = 0
counter = 0
abc = 0
while sum < target:
    sum += nums[i]
    print(i, sum)
    abc += 1
    low += 1
    i += 1
print(i - 1, 'Nothing')



