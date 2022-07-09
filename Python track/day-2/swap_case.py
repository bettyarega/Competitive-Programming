def swap_case(s):
    modified_s = ""
    for i in range(len(s)):
        if(s[i].islower()):
            modified_s +=s[i].upper()
        else:
            modified_s +=s[i].lower()
    return modified_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)