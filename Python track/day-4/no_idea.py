if __name__ == "__main__":
    n,m = input().split()
    arr = list(map(int,input().split()))
    set_A = set(map(int,input().split()))
    set_B = set(map(int,input().split()))
    happiness = 0
    for val in arr:
        if val in set_A and val not in set_B:
            happiness += 1
        elif val in set_B:
            happiness -= 1
    print(happiness)