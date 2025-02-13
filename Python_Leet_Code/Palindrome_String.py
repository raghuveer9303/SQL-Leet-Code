class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_text = ''.join(char for char in s if char.isalpha() == True)
        if filter_text.lower() == filter_text[::-1].lower():
            return True
        else:
            return False
    

sol = Solution()    

print(sol.isPalindrome('A man, a plan, a canal: Panama'))