if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
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
        elif month == 5:
            if day >= 1 and day <= 20:
                print("Kim Nguu")
            else:
                print("Song Tu")
        elif month == 6:
            if day >= 1 and day <= 20:
                print("Song Tu")
            else:
                print("Cu Giai")
        elif month == 7:
            if day >= 1 and day <= 22:
                print("Cu Giai")
            else:
                print("Su Tu")
        elif month == 8:
            if day >= 1 and day <= 22:
                print("Su Tu")
            else:
                print("Xu Nu")
        elif month == 9:
            if day >= 1 and day <= 22:
                print("Xu Nu")
            else:
                print("Thien Binh")
        elif month == 10:
            if day >= 1 and day <= 22:
                print("Thien Binh")
            else:
                print("Thien Yet")
        elif month == 11:
            if day >= 1 and day <= 22:
                print("Thien Yet")
            else:
                print("Nhan Ma")
        else:
            if day >= 1 and day <= 21:
                print("Nhan Ma")
            else:
                print("Ma Ket")