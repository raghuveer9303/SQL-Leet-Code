from typing import List 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            hashmap[number]=index

        for idx, num in enumerate(nums):
            need = target - num
            if need in hashmap and hashmap[need] != idx:
                return idx, hashmap[need]
            
        return ''
    

sol = Solution()
print(sol.twoSum([3,2,4],6))
        
