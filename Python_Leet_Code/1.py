from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0 
        j = 1
        while i < len(nums) - 1:
            if nums[i] + nums[j] == target:
                return [i,j]
            else:
                if j < len(nums)-1 :
                    j = j + 1
                    continue
                else:
                    j = i
                    i = i + 1



sol = Solution()
print(sol.twoSum([3,2,4],6))