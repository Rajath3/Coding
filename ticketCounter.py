
# This approach is having time complexity of O(N/K) or O(K)
N = 100
K = 80

arr = list(range(1, N + 1))
print(arr)

x = 0

if N <= K:
    print(arr[-1])

while len(arr) > K:
    if x == 0:
        arr = arr[K:]
    else:
        arr = arr[:-K]
    print(arr)
    x ^= 1

if x == 0:
    print(arr[-1])
else:
    print(arr[0])



# Optimal solution:
# return ((N - 1) % (2 * K)) + 1
# O(1) complexity
