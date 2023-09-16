def check (ip):
    for i in ip:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
           return False
    return len(ip) == 4
if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    ip = input().split('.')
    if check(ip):
       print("YES")
    else:
       print("NO")
