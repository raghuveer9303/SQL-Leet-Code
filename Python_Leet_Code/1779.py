from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        output = -1
        smallest_distance = 100000
        smallest_index = 100000
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                computed_distance = abs(point[0] - x) + abs(point[1] - y)
                if computed_distance < smallest_distance:  
                        smallest_distance = computed_distance
                        smallest_index = index
                
                elif computed_distance == smallest_distance and index < smallest_index:
                        smallest_distance = computed_distance
                        smallest_index = index
        
        if smallest_index == 100000:    
            return output
        else:
            return smallest_index


sol = Solution()
sol.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]])
