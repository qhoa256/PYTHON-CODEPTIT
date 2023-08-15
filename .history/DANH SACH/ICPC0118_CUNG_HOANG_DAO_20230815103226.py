if __name__ == "__main__":
    t = int(input())
    while t > 0:
        day, month = map(int, input().split())
        if month == 1:
            if day >= 1 and day <= 19:
                print("Ma ket")