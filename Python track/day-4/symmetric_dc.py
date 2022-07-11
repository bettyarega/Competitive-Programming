# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(set_N,set_M):
    symmetric_dc_set = set_N ^ set_M
    ordered_lst = sorted(symmetric_dc_set)
    for val in ordered_lst:
        print(val)

if __name__ == "__main__":
    M = int(input())
    set_M = set(map(int,input().split()))
    N = int(input())
    set_N = set(map(int,input().split()))
    symmetric_difference(set_N, set_M)