def getNthFib(n):
    if n < 3:
        return n - 1
    return getNthFib(n - 1) + getNthFib(n - 2)

print(getNthFib(6))



