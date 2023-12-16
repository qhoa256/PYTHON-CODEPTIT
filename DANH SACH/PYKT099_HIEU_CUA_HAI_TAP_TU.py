if __name__ == "__main__":
    file1 = open('DATA1.in', 'r')
    s1 = set()
    for line in file1:
        a = line.split()
        for x in a: 
            s1.add(x.lower())
    file2 = open('DATA2.in', 'r')
    s2 = set()
    for line in file2:
        a = line.split()
        for x in a: 
            s2.add(x.lower())
    for x in sorted(list(s1.difference(s2))):
        print(x, end = ' ')
    print()
    for x in sorted(list(s2.difference(s1))):
        print(x, end = ' ')
    print()