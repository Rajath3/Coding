class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        arr = []

        count = 0
        length = len(nums)
        while i < length:
            if nums[i] != 0:
                count += 1
            else:
                arr.append(count)
                count = 0
            if i == length - 1:
                arr.append(count)

            i += 1
        
        if len(arr) == 1 and arr[0] == length:
            return length - 1
        
        if len(arr) == 1:
            return arr[0]
                
        maxSum = 0
        j = 0
        s = []
        while j < len(arr) - 1:
            maxSum = arr[j] + arr[j + 1]
            s.append(maxSum)
            j += 1

        return max(s)

