
def happyNumber(n):
    arr = str(n)
    while len(arr) > 1 or int(arr) == 7:
        arr = str(sum([int(val) ** 2 for val in arr]))
        if int(arr) == 1:
            return True
    return False

print(happyNumber(1111111))




