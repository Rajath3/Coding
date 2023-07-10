arr = [1, 2, 5, 4, -9]

def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mid = int(len(arr)/ 2)

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    merged = []
    print(left, right)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
             merged.append(right[j])
             j += 1
        
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

print(mergeSort(arr))