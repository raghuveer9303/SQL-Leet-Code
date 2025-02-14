class Solution:
    def returnFib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.returnFib(n-1) + self.returnFib(n-2)
        

sol = Solution()
print(sol.returnFib(5))



### Without recursion

def fib(self, n: int) -> int:
        a = 0 
        b = 1
        if n == 0:
            return a
        elif n == 1:
            return b
        else:
            for n in range (2, n+1):
                c = a + b
                a = b
                b = c
            return b