from itertools import permutations

if __name__ == "__main__":
    s,k = input().split()
    list_permutations = list(permutations(s,int(k)))
    list_permuted = []
    for i in range(len(list_permutations)):
        list_permuted.append(''.join(list_permutations[i]))
    print(list_permuted)
    list_permuted.sort()
    print(*list_permuted,sep='\n')