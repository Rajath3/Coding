arr = [100, 180, 260, 310, 40, 535, 695]
# arr = [4,2,2,2,4]

i = 0
lengthArr = len(arr)
resultArr = [[None, None]] * lengthArr
while i < lengthArr:
    if (i + 1 >= lengthArr):
        resultArr[i] = i
    elif arr[i + 1] > arr[i]:
        resultArr[i] = i
    elif arr[i + 1] < arr[i] and i != 0:
        resultArr[i] = i
    i += 1
print(resultArr)

# Pending
# https://practice.geeksforgeeks.org/problems/stock-buy-and-sell-1587115621/1?page=1&company[]=Flipkart&curated[]=1&sortBy=submissions