from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_count = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if(nums[i] == nums[j+1] and i < j+1):
                    good_count += 1
        
        return good_count