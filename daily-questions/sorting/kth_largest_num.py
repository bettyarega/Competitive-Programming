from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        sortedNums =  sorted(map(int,nums),reverse = True)
        kthLargest = str(sortedNums[k-1])
        return kthLargest