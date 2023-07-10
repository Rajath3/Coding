# Quick sort and merge sort have almost same time complexity in average case
# but the constants do matter sometimes, so quick sort is always faster.

# Quick sort average case is O(n log n) and worst case O(n**2) if the array is already sorted'


arr = [10, 9, 7, 12, -1]

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if i <= pivot]

        greater = [i for i in arr[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)
    
print(quickSort(arr))


