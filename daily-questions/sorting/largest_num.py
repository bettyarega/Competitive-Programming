from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        # print(x)
        # print(y)
        return x+y > y+x

class Solution:
    # def compare(self,num):
    #     return a + b > b + a
    def largestNumber(self, nums: List[int]) -> str:
        largest = ''.join(sorted(map(str,nums), key = LargerNumKey))
        if largest[0] == '0':
            return '0'
        else:
            return largest