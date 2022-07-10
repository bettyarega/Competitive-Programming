if __name__ == "__main__":
    set_country = set()
    for _ in range(int(input())):
        country = input()
        set_country.add(country)
    print(len(set_country))
