class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == 0:
            return 0
        else:
            if (high - low)%2 == 0:
                if high%2 == 0:
                    return (high - low)//2
                else:
                    return ((high - low)//2) + 1
            else: 
                return ((high - low)//2) + 1
