arr = [4, 0, 2, 1, 3]



n = len(arr) - 1
# newArr = [None] * length
# for i in range(n):
for i in range(n):
    index = arr[i] // n
    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp

print(arr)