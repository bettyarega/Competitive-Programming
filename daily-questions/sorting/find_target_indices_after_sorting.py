class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if(nums[j] > nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
                
    
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_arr = self.sort(nums)
        target_indices = []
        for i in range(len(sorted_arr)):
            if(sorted_arr[i] == target):
                target_indices.append(i)
        return target_indices

Solution().targetIndices([5,4,3,3,1,1,2],3)