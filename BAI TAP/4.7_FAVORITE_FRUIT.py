if __name__ == "__main__":
  favorite_fruits = ["Banana", "Apple", "Coconut"]

  for i in range(5):
    fruit = input()
    if fruit in favorite_fruits:
      print("You really like", fruit)