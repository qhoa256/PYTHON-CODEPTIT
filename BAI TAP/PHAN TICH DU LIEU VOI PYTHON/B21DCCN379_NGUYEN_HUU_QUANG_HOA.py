import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Salaries.csv")
#Cau 1
#Tìm giá trí lớn nhất, nhỏ nhất, trung bình theo tên cột được nhập vào (với các cột kiểu số)
inp = input("Nhap vao truong du lieu muon tinh: ")
print(df[inp].max(), df[inp].min(), df[inp].mean())
#Ve bieu do cho min, max, mean su dung Scarter
plt.scatter([1, 2, 3], [df[inp].max(), df[inp].min(), df[inp].mean()])
plt.title("Bieu do scatter min, max, mean: " + inp)
plt.show()

#Cau 2
# Hiển thị biểu đồ biến thiên ngày tháng và distance(flights.csv); biểu đồ thống kê sex đạng cột (Salaries.csv);
dfFlight = pd.read_csv("flights.csv")
dfFlight['date'] = pd.to_datetime(dfFlight[['day', 'month', 'year']])
plt.plot(dfFlight['date'], dfFlight['distance'])
plt.xlabel("Ngay thang")
plt.ylabel("Distance")
plt.title("Bieu do bien thien ngay thang va distance: ")
plt.show()

# Hien thi bieu do thong ke sex theo cot trong file Salaries.csv
df['sex'].value_counts().plot(kind='bar')
plt.title("Thong ke gioi tinh")
plt.show()

#Cau 3
# Sắp xếp dữ liệu theo tên cột được nhập vào, vẽ và hiễn thị biểu đồ tương ứng
column = input("Nhap ten cot du lieu muon sap xep: ")
df = df.sort_values(by = column)
plt.plot(df[column], df['salary'])
plt.xlabel(column)
plt.ylabel("Salary")
plt.title("Bieu do bien thien " + column + " va salary")
plt.show()