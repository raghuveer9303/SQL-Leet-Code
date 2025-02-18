from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        output = []
        ## Forming the hashmap
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1 
            else:
                hashmap[num] = 1

        for i in range(0,k):
            max_key = max(hashmap, key=hashmap.get)
            output.append(max_key)
            del hashmap[max_key]
    
        return output


    
sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))