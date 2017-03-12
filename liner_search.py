def linear_search(list, item):
    for x in list:
        if x == item:
            return True
    return False

if __name__ == '__main__':
    from random import shuffle
    l = [1, 2, 3, 4]
    print(l)
    v = int(input('Find Value?'))
    r = linear_search(l, int(v))
    if r:
        print("Found!")
    else:
        print("Not Found!")
