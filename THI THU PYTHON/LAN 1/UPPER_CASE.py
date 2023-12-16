if __name__ == "__main__":
    s = input()
    qhoa = list(s.strip().split())
    for x in qhoa:
        print(x[0].upper() + x[1::], end = '')