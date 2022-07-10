if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    s_sum = 0
    for i in range(m):
        command, *line = input().split()
        val = list(map(int,line))
        if(command == "pop"):
            s.pop()
        elif(command == "remove"):
            s.remove(val[0])
        elif(command == "discard"):
            s.discard(val[0])
    for val in s:
        s_sum += val
    print(s_sum)