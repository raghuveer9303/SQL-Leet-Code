from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        coin_count = 0

        for coin in coins:
            used_coin = amount//coin
            amount = amount%coin
            coin_count = coin_count + used_coin

        if amount > 0:
            return -1
        else:
            return coin_count



sol = Solution()
print(sol.coinChange([186,419,83,408],6249))