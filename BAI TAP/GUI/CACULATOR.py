import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')

# Tạo khung chứa các nút và ô nhập
frame = tk.Frame(master=window, bg="lightgray", padx=10, pady=10)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=25, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, ipady=10)

# Hàm để thêm số vào ô nhập
def myclick(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Hàm để tính toán biểu thức và hiển thị kết quả
def equal():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", "Lỗi cú pháp hoặc phép tính không hợp lệ.")

# Hàm để xóa nội dung trong ô nhập
def clear():
    entry.delete(0, tk.END)

# Tạo nút số và nút phép tính
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(master=frame, text=button, padx=15, pady=15, width=5, font=("Arial", 16), command=equal).grid(row=row_val, column=col_val)
    elif button == '0':
        tk.Button(master=frame, text=button, padx=15, pady=15, width=5, font=("Arial", 16), command=lambda b=button: myclick(b)).grid(row=row_val, column=col_val)
    else:
        tk.Button(master=frame, text=button, padx=15, pady=15, width=5, font=("Arial", 16), command=lambda b=button: myclick(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút xóa
tk.Button(master=frame, text="C", padx=15, pady=15, width=5, font=("Arial", 16), command=clear).grid(row=5, column=0, columnspan=2)

# Main loop
window.mainloop()
