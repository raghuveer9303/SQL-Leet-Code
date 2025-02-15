from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        j = n - 1
        max_qty = 0
        i = 0
        while i < j:
            computed_quantity = min(height[i],height[j]) * (j-i)
            if computed_quantity > max_qty:
                max_qty = computed_quantity
            
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        
        return max_qty

height = [1,8,6,2,5,4,8,3,7]

sol = Solution()
print(sol.maxArea(height))
