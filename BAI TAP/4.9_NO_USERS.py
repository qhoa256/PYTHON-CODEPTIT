if __name__ == "__main__":
  users = ["admin", "Hoa", "Dat", "Manh", "Anh", "Lan", "Hung", "Trong", "Hai", "Mai"]
  for x in users:
    if x == "admin":
      print("Hello admin! Do you want to see status report?")
    else:
      print("Hello", x, "Thank you for logging in this website!")
  else:
      print("We need to find some users!")
  
  # Remove all users
  users.clear()

  if users:
    for x in users:
      if x == "admin":
        print("Hello admin! Do you want to see status report?")
      else:
        print("Hello", x, "Thank you for logging in this website!")
  else:
    print("We need to find some users!")