from itertools import combinations

if __name__ == "__main__":
    s, k = input().split()
    for i in range(1,int(k)+1):
        for j in combinations(sorted(s),i):
            print("".join(j))

            
    # list_combinations = list(combinations(s,int(k)))
    # list_combined = list(s)
    # print(list_combined)
    # for i in range(len(list_combinations)):
    #     list_combined.append(''.join(list_combinations[i]))
    # list_combined.sort()
    # print(*list_combined,sep='\n')