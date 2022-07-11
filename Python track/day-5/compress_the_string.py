from itertools import groupby

if __name__ == "__main__":
    s = list(input())
    for key, grp in groupby(map(int,s)):
        print(tuple([len(list(grp)),key]), end= ' ')