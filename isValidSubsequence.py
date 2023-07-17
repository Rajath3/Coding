def isValidSubsequence(array, sequence):
    currentPtr = 0
    seqPtr = 0
    while currentPtr <= len(array) - 1:
        print(currentPtr,seqPtr, len(sequence))
        if sequence[seqPtr] == array[currentPtr]:
            seqPtr += 1
            if seqPtr == len(sequence):
                return True
        currentPtr += 1
    return False
    
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [22, 25, 6]
print(isValidSubsequence(array, sequence))