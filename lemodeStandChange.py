N = 5
# resArr = [5, 5, 10, 10, 20]
resArr = [5, 5, 5, 10, 20]
fixedPrice = 5
hash = {}
flag = 0

for i in range(N):
    if resArr[i] > fixedPrice:
        cChange = resArr[i] - fixedPrice
        sum = 0
        sumArr = []

        for j in range(0, i):
            sum += resArr[j]
            sumArr.append(sum)
            if sum == cChange:
                while j == 0:
                    resArr[j] = 0
                    j -= 1
            elif j == i - 1:
                flag = 1
        print(sumArr)

if flag == 1:
    print("Not possible")
else:
    print("Possible")
            
print(resArr)
            



        
    