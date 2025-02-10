from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        total = len(salary) - 2 
        avg = sum(salary[1:-1])/total
        return avg  