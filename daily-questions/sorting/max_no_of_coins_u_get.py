from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3::2])
        
    
        # maxSum = 0
        # sorted(piles)
        # for i in range(len(piles)//3, len(piles), 2):
        #     maxSum += piles[i]
        # return maxSum
        