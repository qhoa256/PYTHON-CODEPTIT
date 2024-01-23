#D
d = dict()

for x in books:
    if x['author'] in d:
        d[x['author']] += 1
    else:
        d[x[x['author']]] = 1

# In ra thông tin sách của các tác giả có nhiều hơn 2 cuốn
for author, count in d.items():
    if count > 2:
        print(author)
        for x in books:
            if x['author'] == author:
                print(x)
#E
# Cho tat ca cac ma sach da duyet qua vao SET, duyet qua cac ma sach va kiem tra xem da ton
# tai tron Set chua, neu ton tai roi thi tuc la co 2 quyen sach co trung ma
se = set()
ok = False
for x in books:
    if x['code'] in se:
        ok = True
        break
    se.add(x['code'])

if ok:
    print("YES")
else:
    print("NO")
#F
# Sort theo dieu kien dung bieu thuc Lambda
books = sorted(books, key=lambda x: x['name'])
for book in sorted_books:
    print(book)