#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        return sum(number**3 for number in range(1,n+1))


sol = Solution()

print(sol.sumOfSeries([1,2,3,4,5]))