import sys
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    highScore = -sys.maxsize - 1
    runnerUpScore = -sys.maxsize - 1
    arrList = list(arr)
    for i in range(n):
        if(arrList[i] > highScore):
            highScore = arrList[i]
    for i in range(n):
        if(arrList[i] < highScore and arrList[i]>runnerUpScore):
            runnerUpScore = arrList[i]
    print(runnerUpScore)