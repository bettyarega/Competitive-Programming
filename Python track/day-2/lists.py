if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        command, *line = input().split()
        values =list( map(int,line))
        if(command == 'insert'):
            arr.insert(values[0],values[1])
        elif(command == 'print'):
            print(arr)
        elif(command == 'remove'):
            arr.remove(values[0])
        elif(command == 'append'):
            arr.append(values[0])
        elif(command == 'sort'):
            arr.sort()
        elif(command == 'pop'):
            arr.pop()
        elif(command == 'reverse'):
            arr.reverse()
