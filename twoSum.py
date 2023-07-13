array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

resultArr = []
for i in range(len(array)):
    for j in range(len(array)):
        sum = array[i] + array[j]
        if sum == targetSum and array[i] != array[j]:
            if not array[i] in resultArr:
                resultArr.append(array[i])
            if not array[j] in resultArr:
                resultArr.append(array[j])
print(resultArr)

## Hash approach

hash = {}

for val in array:
    match = targetSum - val
    if match in hash:
        print([val, match])
        break
    else:
        hash[val] = True

print([])

# Sorted approach

array.sort()
l = 0
r = len(array) -1

while l < r:
    sum = array[l] + array[r]
    if sum == targetSum:
        print([array[l], array[r]])
    elif sum < targetSum:
        l += 1
    else:
        r -= 1 

