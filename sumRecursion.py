arr = [2, 4, 6, 8]

# sum of array
def arrSum(arr, sum):
    if arr == []:
        print(sum) 
    else:
        sum += arr.pop(0)
        arrSum(arr, sum)

arrSum(arr, sum = 0)


arr = [2, 4, 6, 8]
# count number of items in list
def countList(arr, count):
    if arr == []:
        print(count)
    else:
        arr.pop(0)
        count += 1
        countList(arr, count)
countList(arr, count = 0)


arr = [2, 4, 6, 8]
# max number in list

def maxInList(arr, max):
    if arr == []:
        print(max)
    else:
        num = arr.pop(0)
        if num > max:
            max = num
        maxInList(arr, max)
maxInList(arr, max = -999999999)