def ex3_1():
  names = ["Trần Quý Đạt", "Nguyễn Thị Lan", "Nguyễn Hữu Quang Hòa", "Bùi Thị Lan Phương", "Nguyễn Hoàng Hải"]
  for name in names:
    print(name)
  print()

def ex3_2():
  names = ["Trần Quý Đạt", "Nguyễn Thị Lan", "Nguyễn Hữu Quang Hòa", "Bùi Thị Lan Phương", "Nguyễn Hoàng Hải"]
  for name in names:
    print(f"Chào {name}! Chúc bạn một ngày tốt lành!")
  print()

def ex3_3():
  vehicles = ["G65", "Honda CBR1000RR", "Toyota Fortuner", "Vespa Primavera", "Boeing 747", "Tesla Model X"]
  for vehicle in vehicles:
    print(f"I would like to own a {vehicle}.")
  print()

def ex3_4():
  guests = ["Darkness", "Aqua", "Megumin"]
  for guest in guests:
    print(f"Chào {guest}! Bạn có muốn dùng bữa tối cùng tôi không?")
  print()

def ex3_5():
  guests = ["Quang Hòa", "Hoàng Hải", "Quý Đạt", "Thị Lan"]
  for guest in guests:
    print(f"Chào {guest}! Tôi muốn mời bạn tham gia bữa tối cùng tôi !")

  unavailable_guest = "Thị Lan"
  print(f"\n {unavailable_guest} không thể tham gia bữa tối.\n")

  guests[guests.index(unavailable_guest)] = "Phương Mai"
  
  for guest in guests:
    print(f"Chào {guest}! Tôi muốn mời bạn tham gia bữa tối cùng tôi!")
  print()

def ex3_6():
  guest_list = ["Quý Đạt", "Quang Hòa", "Thị Lan"]
  for guest in guest_list:
    print(f"Chào {guest}, bạn có muốn tham gia bữa tối cùng tôi vào cuối tuần này không?")
  guest_list.insert(0, "Hải")
  guest_list.insert(2, "Thắng")
  guest_list.append("Phương Mai")
  print("Chúng tôi vừa tìm được một bàn ăn lớn hơn, nên chúng ta có thêm chỗ cho mọi người!")
  for guest in guest_list:
    print(f"Dear {guest}, bạn có mời tham gia bữa tối cùng tôi vào cuối tuần này không?")

def ex3_7():
  guest_list = ["Quý Đạt", "Quang Hòa", "Thị Lan", "Tiến Thắng"]
  print("Chúng tôi vừa tìm được một bàn ăn lớn hơn, nên chúng ta có thêm chỗ cho mọi người!")
  for guest in guest_list:
    print(f"Dear {guest}, bạn có mời tham gia bữa tối cùng tôi vào cuối tuần này không?")
  print("Xin lỗi, nhưng chúng tôi chỉ có thể mời 2 khách.")
  while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Xin lỗi, {removed_guest}, bạn không thể tham gia bữa tối.")

  for guest in guest_list:
    print(f"Dear {guest}, bạn vẫn được mời tham gia bữa tối cùng tôi vào cuối tuần này.")

  del guest_list[-1]
  del guest_list[-1]

  print("Danh sách khách sau khi xóa:", guest_list)

def ex3_8():
  locations = ["Paris", "New York", "Tokyo", "Sydney", "London"]

  print("Danh sách địa điểm ban đầu:")
  for location in locations:
    print(location)

  print("\nDanh sách địa điểm theo thứ tự bảng chữ cái:")
  for location in sorted(locations):
    print(location)

  print("\nDanh sách địa điểm sau khi in lại:")
  for location in locations:
    print(location)

  print("\nDanh sách địa điểm theo thứ tự ngược của bảng chữ cái:")
  for location in sorted(locations, reverse = True):
    print(location)

  print("\nDanh sách địa điểm sau khi in lại:")
  for location in locations:
    print(location)

  locations.reverse()
  print("\nDanh sách địa điểm sau khi đảo ngược:")
  for location in locations:
    print(location)

  locations.reverse()
  print("\nDanh sách địa điểm sau khi đổi về ban đầu:")
  for location in locations:
    print(location)

  locations.sort()
  print("\nDanh sách địa điểm sau khi sắp xếp theo bảng chữ cái:")
  for location in locations:
    print(location)

  locations.sort(reverse = True)
  print("\nDanh sách địa điểm sau khi sắp xếp ngược bảng chữ cái:")
  for location in locations:
    print(location)

def ex3_9():
  locations = ["Paris", "New York", "Tokyo", "Sydney", "London"]
  print(f"Số lượng địa điểm trong danh sách là:", len(locations))

def ex3_10():
  places = ["Mount Everest", "Amazon River", "United States", "Paris", "Victoria Falls"]
  print("Danh sách các địa danh ban đầu:")
  print_places(places)

  places.append("New York")

  print("\nDanh sách sau khi thêm New York:")
  print_places(places)

  places.insert(1, "Canada")

  print("\nDanh sách sau khi thêm Canada:")
  print_places(places)

  places.remove("Mount Everest")

  print("\nDanh sách sau khi xóa Mount Everest:")
  print_places(places)

  places.sort()

  print("\nDanh sách sau khi sắp xếp theo thứ tự bảng chữ cái:")
  print_places(places)

  places.reverse()

  print("\nDanh sách sau khi đảo ngược thứ tự:")
  print_places(places)

  places.pop()

  print("\nDanh sách sau khi xóa phần tử cuối cùng:")
  print_places(places)

def print_places(places):
  for place in places:
    print(place)

def ex3_11():
  favorite_pizzas = ["Pepperoni", "Margherita", "Hawaiian"]
  print("Danh sách các loại pizza ưa thích:")
  for pizza in favorite_pizzas:
    print(f"I like {pizza} pizza.")
  print("I really love pizza!")

def ex3_12():
  animals = ["Dog", "Cat", "Bird"]
  print("Các loài động vật có đặc điểm chung:")
  for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")
  print("Any of these animals would make a great pet!")


def ex3_13():
  for number in range(1, 21):
    print(number)

def ex3_14():
  a = list(range(1, 1000001))
  for number in a:
    print(number)
  
def ex3_15():
  numbers = list(range(1, 1000001))

  min_value = min(numbers)
  max_value = max(numbers)

  total_sum = sum(numbers)

  print(f"Min: {min_value}")
  print(f"Max: {max_value}")
  print(f"Total Sum: {total_sum}")

def ex3_16():
  odd_numbers = list(range(1, 21, 2))
  print("Các số lẻ từ 1 đến 20:")
  for number in odd_numbers:
    print(number)

def ex3_17():
  multiples_of_3 = list(range(3, 31, 3))
  print("Các bội số của 3 từ 3 đến 30:")
  for number in multiples_of_3:
    print(number)

def ex3_18():
  cubes = [number ** 3 for number in range(1, 11)]
  print("10 số lập phương đầu tiên:")
  for cube in cubes:
    print(cube)

def ex3_19():
  cubes = [number ** 3 for number in range(1, 11)]
  print("10 số lập phương đầu tiên:")
  for cube in cubes:
    print(cube)

def ex3_20():
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  print("The first three items in the list are:", my_list[:3])
  
  middle_start = len(my_list) // 2 - 1
  middle_end = middle_start + 3
  print("Three items from the middle:", my_list[middle_start:middle_end])

  print("The last three items in the list are:", my_list[-3:])

def ex3_21():
  my_pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

  friend_pizzas = my_pizzas[:]

  my_pizzas.append("Vegetarian")

  friend_pizzas.append("Supreme")

  print("My favorite pizzas are:")
  for pizza in my_pizzas:
    print(pizza)

  print("\nMy friend's favorite pizzas are:")
  for pizza in friend_pizzas:
    print(pizza)


def ex3_22():
  my_foods = ["Pizza", "Burger", "Pasta", "Sushi", "Ice Cream"]

  your_foods = ["Salad", "Burger", "Pasta", "Fried Chicken", "Ice Cream"]

  print("My favorite foods:")
  for food in my_foods:
    print(food)

  print("\nYour favorite foods:")
  for food in your_foods:
    print(food)

def ex3_23():
  menu = ("Pizza", "Burger", "Pasta", "Sushi", "Ice Cream")

  print("Danh sách các món ăn của cửa hàng buffet:")
  for food in menu:
    print(food)

  new_menu = ("Salad", "Burger", "Steak", "Sushi", "Dessert")

  print("\nDanh sách các món ăn sau khi thay đổi thực đơn:")
  for food in new_menu:
    print(food)


if __name__ == '__main__':
  ex3_1()
  ex3_2()
  ex3_3()
  ex3_5()
  ex3_5()
  ex3_6()
  ex3_8()
  ex3_9()
  ex3_10()
  ex3_11()
  ex3_12()
  ex3_13()
  ex3_14()
  ex3_15()
  ex3_16()
  ex3_17()
  ex3_18()
  ex3_19()
  ex3_20()
  ex3_21()
  ex3_22()
  ex3_23()
