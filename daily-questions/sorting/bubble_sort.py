import math
import os
import random
import re
import sys

def countSwaps(a):
    no_of_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if(a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                no_of_swaps += 1
    print('Array is sorted in ' + str(no_of_swaps) + ' swaps.')
    print('First Element: ' + str(a[0]) + ' ')
    print('Last Element: ' + str(a[-1]) + ' ')
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)