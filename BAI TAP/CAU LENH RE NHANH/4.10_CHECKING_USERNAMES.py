if __name__ == "__main__":
  current_users = ["admin", "Hoa", "Dat", "Manh", "Anh", "Lan", "Hung", "Trong", "Hai", "Mai"]
  new_users = ["Tien", "Thanh", "Khanh", "Hoa", "Hang", "Tu", "Dat", "Phuong", "Thao", "Thuy"]
  lower_users = list(map(lambda x: x.lower(), current_users))
  for x in new_users:
    if x.lower() in lower_users:
      print("Username is already taken. Please enter a new username!")
    else:
      print("Username available.")

