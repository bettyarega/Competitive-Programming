from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        noOfOperations = 0
        valMap = {}
        for val in nums:
            x = k - val
            if x in valMap and valMap[x] > 0:
                noOfOperations += 1
                valMap[x] -=1
            else:
                if val in valMap:
                    valMap[val] += 1
                else:
                    valMap[val] = 1
        return noOfOperations
                    
                
            
            
 #first try===============         
#         noOfOperations = 0
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 continue
#             for j in range(i+1,len(nums),1):
#                 if nums[j] == 0:
#                     continue
#                 if nums[i] + nums[j] == k:
#                     noOfOperations += 1
#                     nums[i] = 0
#                     nums[j] = 0
#                     break
#         return noOfOperations