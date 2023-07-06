# Time complexity O(n**2)
# Even though the original array size decreases , we ignore the 
# constants while considering Big O

arr = [3, 4, 5, 1, 2]

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for j in range(1, len(arr)):
        if arr[j] < smallest:
            smallest = arr[j]
            smallest_index = j
    return smallest_index


newArr = []
for i in range(0, len(arr)):
    smallest = findSmallest(arr)
    newArr.append(arr.pop(smallest))
print(newArr)



