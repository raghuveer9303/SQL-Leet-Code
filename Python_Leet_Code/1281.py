class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        for s in str(n):
            sum = sum + int(s)
            product = product * int(s)
        
        return product - sum