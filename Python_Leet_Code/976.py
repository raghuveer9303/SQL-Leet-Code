from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        max_perimeter = 0
        if len(nums) < 3:
            return 0
        else:
            for num in range(0,len(nums)-2):
                if nums[num+1] and nums[num+2]: 
                    if nums[num] < nums[num+1] + nums[num+2]:
                        if (nums[num] + nums[num+1] + nums[num+2]) > max_perimeter:
                            max_perimeter = (nums[num] + nums[num+1] + nums[num+2])
        
        return max_perimeter
    

nums = [7,5,2,3,11]
sol = Solution()
print(sol.largestPerimeter(nums))