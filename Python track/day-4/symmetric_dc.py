# Enter your code here. Read input from STDIN. Print output to STDOUT
def symmetric_difference(set_N,set_M):
    symmetric_dc_set = set_N ^ set_M
    ordered_lst = sorted(symmetric_dc_set)
    for val in ordered_lst:
        print(val)

if __name__ == "__main__":
    M = int(input())
    list_M = input().split()
    set_M = set(map(int,list_M))
    N = int(input())
    list_N = input().split()
    set_N = set(map(int,list_N))
    symmetric_difference(set_N, set_M)