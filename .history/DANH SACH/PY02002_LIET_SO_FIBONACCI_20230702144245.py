F = [0] * 93

def init():
    F[1] = 1
    F[2] = 1
    for i in range(3, 93):
        F[i] = F[i - 1] + F[i - 2]

if __name__ == "__main__":
    init()
    t = int(input())
    while t != 0:
        
