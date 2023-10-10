if __name__ == "__main__":
  age = int(input())
  if age < 2:
    print("Baby")
  elif age <= 4:
    print("Toddler")
  elif age <= 13:
    print("Kid")
  elif age <= 20:
    print("Teenager")
  elif age <= 65:
    print("Adult")
  else:
    print("Elder")