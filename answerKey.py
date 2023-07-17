# leetcode 2024

answerKey = "TTFFFT"
k = 2

arr = list(answerKey)
eligibleElem = 'T' if arr.count('T') > arr.count('F') else 'F'

for i in range(1, len(arr)):
    if arr[i - 1] == eligibleElem:
        if arr[i] != eligibleElem:
            arr[i] = eligibleElem
    else:
        if eligibleElem == 'T':
            arr[i] = 'F'
        else:
            arr[i] = 'T'
    
    max1 = -99999
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == eligibleElem:
            count += 1
            max1 = max(max1, count)
    print(max1)

