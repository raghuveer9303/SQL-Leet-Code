from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
        
        max_key = max(hashmap, key=hashmap.get)

        m = hashmap[max_key]

        if m == 1:
            return len(nums)

        output = 0

        for key, num in hashmap.items():
            if num > m:
                m = num
            elif num == m:
                output = output + num
        
        return m
    

sol = Solution()
print(sol.maxFrequencyElements([1,2,2,3,1,4]))