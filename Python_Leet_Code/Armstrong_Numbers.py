
class Solution:
    def armstrongNumber (self, n):
        number = str(n)
        power = sum(int(num)**3 for num in number)
        
        if n == power:
            return True
        else: 
            return False
