
s = "ab"
goal = "ba"

lengthS = len(s)
lengthGoal = len(goal)

if lengthS != lengthGoal or lengthS == 1:
    print(False)

hashS = {}
hashGoal = {}
count = 0
for i in range(0, lengthS):
    if s[i] in hashS:
        hashS[s[i]] += 1
    else:
        hashS[s[i]] = 1

    if goal[i] in hashGoal:
        hashGoal[goal[i]] += 1
    else:
        hashGoal[goal[i]] = 1

    if s[i] != goal[i]:
        count += 1
        if count > 2:
            print(False)
allEqualCount = next(iter(hashS.values()))
x = True
if len(hashS) == 1:
    print(True)

for key in hashS:
    if not key in hashGoal:
        print(False)
    if hashS[key] != hashGoal[key]:
        print(False)
    if allEqualCount != hashGoal[key]:
        x = False 
    
if count == 2 or (allEqualCount > 1 and x == True) or (count == 0 and x == False):
    print(True)
else:
    print(False)


# Actual solution i
# 1. if s and goal are equal then check any character is repeating, if so then retrun true
# 2. if not check difference and print( accordingly
