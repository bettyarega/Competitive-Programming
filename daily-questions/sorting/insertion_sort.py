import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    temp = arr[n-1]
    for i in reversed(range(n)):
        if(temp < arr[i - 1] and i != 0):
            arr[i] = arr[ i - 1]
        else:
            arr[i] = temp
            print(*arr, sep = ' ')
            break
            
        print(*arr, sep = ' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
