class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_count = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(j != i and nums[j] < nums[i]):
                    count +=1
            nums_count.append(count)
        return nums_count

Solution().smallerNumbersThanCurrent([8,1,2,2,3])