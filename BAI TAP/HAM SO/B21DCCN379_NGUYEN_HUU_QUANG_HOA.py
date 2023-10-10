def display_message():
  print("Function")

def favourite_book(title):
  print(title)

def make_shirt(size, message):
  print(size)
  print(message)

def description_city(city, country = "Vietnam"):
  print(city, "is in", country)

def city_country(city, country):
  return f"{city}, {country}"

def make_album(artist_name, album_title, num_songs = None):
  album_info = {
      'artist': artist_name,
      'title': album_title,
  }
  if num_songs is not None:
      album_info['num_songs'] = num_songs
  return album_info

def show_messsages(messages):
  for x in messages:
    print(x, end = '  ')

sent_messages = []

def send_message(messages, sent_messages):
  while messages:
      message = messages.pop()
      print(f"Sending message: {message}")
      sent_messages.append(message)

def send_message(messages, sent_messages):
  while messages:
      message = messages.pop()
      print({message})
      sent_messages.append(message)

def make_sandwich(*items):
  print("\nSandwiches:")
  for item in items:
      print("- " + item)

def make_car(manufacturer, model, **car_info):
  car = {
      'manufacturer': manufacturer,
      'model': model,
  }
  for key, value in car_info.items():
      car[key] = value
  return car

if __name__ == "__main__":
  #7.1
  display_message()
  #7.2
  favourite_book("A Certain Magical Index")
  #7.3
  make_shirt("L", "I crush NM")
  make_shirt(message = "Hai love Mai", size = "XL")
  #7.4
  make_shirt("XXL", message="I love Python")
  make_shirt("L", message="I love Python")
  make_shirt("S", "I love Deep Learning")
  #7.5
  description_city("Ha Noi")
  description_city("Hung Yen")
  description_city("Tokyo", "Japan")
  #7.6
  print(city_country("Ha Noi", "Viet Nam"))
  #7.7
  album1 = make_album('Aimer', 'Distance')
  album2 = make_album('Alan Walker', 'Lily')
  album3 = make_album('LiSA', 'Gurenge', num_songs = 25)
  print(album1, album2, album2)
  #7.8
  while True:
    artist = input()
    if artist == 'q':
       break
    title = input()
    num_songs = int(input())
    album = make_album(artist, title, num_songs)
    print(album)
  #7.9
  messages = ["I love you", "Football is coming home", "Detective Conan is a special book"]
  show_messsages(messages)
  #7.10
  send_message(messages, sent_messages)
  for x in sent_messages:
     print(x)
  #7.11
  messages_copy = messages.copy()
  send_message(messages_copy, sent_messages)
  for x in messages:
     print(x)
  for x in sent_messages:
     print(x)
  #7.12
  make_sandwich("Thịt gà", "Rau diếp", "Sốt mayo")
  make_sandwich("Thịt bò", "Phô mai", "Hành tây", "Dưa leo")
  make_sandwich("Trứng", "Bacon", "Cà chua", "Sốt sriracha", "Bơ lạt")
  #7.13
  car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

