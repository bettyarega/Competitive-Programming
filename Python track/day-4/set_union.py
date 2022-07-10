if __name__ == "__main__":
    n = int(input())
    set_n = set(map(int,input().split()))
    b = int(input())
    set_b = set(map(int,input().split()))
    set_union = set_n | set_b
    print(len(set_union))