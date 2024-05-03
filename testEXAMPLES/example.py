def fill(coll, value, begin=0, end=None):
    if begin > len(coll):
        return coll
    if end is None:
        while begin < len(coll):
            coll[begin] = value
            begin += 1
    else:
        while begin < end:
            coll[begin] = value
            begin += 1
    return coll


def main():
    coll = [1, 2, 3, 4]
    
    fill(coll, '*', 1, 3)
    print(coll)  # => [1, '*', '*', 4]
    
    fill(coll, '*')
    print(coll)  # => ['*', '*', '*', '*']
    
    fill(coll, '*', 4)
    print(coll)  # => [1, 2, 3, 4]
    
    fill(coll, '*', 0, 10)
    print(coll)  # => ['*', '*', '*', '*']


if __name__ == '__main__':
    main()
