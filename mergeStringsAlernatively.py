# accepted

word1 = "abcd"
word2 = "pq"

wordOne = list(word1)
wordTwo = list(word2)

len1 = len(wordOne)
len2 = len(wordTwo)

greaterLen = len1 if len1 >= len2 else len2
               
resultArr = []
for i in range(0, greaterLen):
   if i < len1:
      resultArr.append(wordOne[i]) 
   
   if i < len2:
      resultArr.append(wordTwo[i]) 

print(''.join(resultArr))

# Can do two pointer approach as well.