if __name__ == "__main__":
  ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  for x in ordinal_numbers:
    if x == 1:
      print(x, "st", sep = "")
    elif x == 2:
      print(x, "nd", sep = "")
    elif x == 3:
      print(x, "rd", sep = "")
    else:
      print(x, "th", sep = "")