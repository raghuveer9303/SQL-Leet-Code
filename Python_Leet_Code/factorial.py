
class Solution:
    def factorialNumbers(self, n):
        factors = []
        if n == 1:
            return [1]
        
        factorial = 1  
        for x in range(1, n + 1):
            factorial = factorial * x
            if factorial > n:
                break

            factors.append(factorial)
        return factors

sol = Solution()
print(sol.factorialNumbers(5))    