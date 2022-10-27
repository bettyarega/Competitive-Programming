from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) ->List[bool]:
        val = 0
        answer = []
        for i in range(len(l)):
            subA = nums[l[i]:r[i]+1]
            subA.sort()
            
            difference = subA[1] - subA[0]
            for i in range(len(subA)-1):
                if(subA[i+1] - subA[i] != difference):
                    b = 0
                    break
                else:
                    b = 1
            if b == 1:
                answer.append(True)
            else:
                answer.append(False)
        return answer
        