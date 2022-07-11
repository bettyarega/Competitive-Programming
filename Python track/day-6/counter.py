from collections import Counter

if __name__ == "__main__":
    x = int(input())
    shoe_sizes_x = input().split()
    n = int(input())
    money = 0
    for i in range(n):
        shoe_size, price = input().split()
        if(shoe_size in shoe_sizes_x):
            shoe_sizes_x.remove(shoe_size)
            money += int(price)
            
    print(money)