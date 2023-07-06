# Brute force approach
s = "aaaabbaa"
# s = "aaaabbbaaabbbaaabbbcccccccllldghd"
# {1: 'd', 2: 'll', 3: 'lll', 4: 'cccc', 9: 'bbbaaabbb', 15: 'bbbaaabbbaaabbb', 7: 'ccccccc', 13: 'bbaaabbbaaabb', 5: 'ccccc', 11: 'baaabbbaaab', 6: 'cccccc'}
    
length = len(s)
res = {}
for i in range(0, length):
    j = i + 1
    for j in range(j, length + j):
        str = s[i:j]
        values = res.values()
        if str == str[::-1]:
            if not len(str) in res:
                res[len(str)] = str
print(res[max(res.keys())])


