class Solution: 
    def select(self, arr, i):
        num = arr[i]
    
    def selectionSort(self, arr,n):
        for i in range(n-1):
            min = i;
            for j in range(i+1,n):
                if arr[j] < arr[min]:
                    min = j
                    
            if min != i:
                temp = arr[i]
                arr[i] = arr[min]
                arr[min] = temp        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end= ' ')

        print()