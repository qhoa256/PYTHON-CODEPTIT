if __name__ == "__main__":
    t = int(input())
    while t > 0:
        day, month = map(int, input().split())
        if month == 1:
            if day >= 1 and day <= 19:
                print("Ma Ket")
            else:
                print("Bao Binh")
        elif month == 2:
            if day >= 1 and day <= 18:
                print("Bao Binh")
            else:
                print("Song Ngu")
        elif month == 3:
            if day >= 1 and day <= 20:
                print("Song Ngu")
            else:
                print("Bach Duong")
        elif month == 4:
            if day >= 1 and day <= 19:
                print("Bach Duong")
            else:
                print("Kim Nguu")
        elif month == 