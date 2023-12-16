import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, Toplevel

class Employee:
    def __init__(self, emp_id, name, salary, dept_id, dept_name):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.dept_id = dept_id
        self.dept_name = dept_name

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Nhân Viên")
        self.existing_emp_ids = set()
        self.employees = []

        self.create_widgets()
    
    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=('Arial', 12))
        style.configure("TLabel", font=('Arial', 12))

        # Tạo các label và entry widgets để nhập thông tin nhân viên
        label1 = ttk.Label(self.root, text="Mã số:")
        label1.grid(row=0, column=0, padx=10, pady=10)

        self.emp_id_entry = ttk.Entry(self.root)
        self.emp_id_entry.grid(row=0, column=1, padx=10, pady=10)

        label2 = ttk.Label(self.root, text="Họ tên:")
        label2.grid(row=1, column=0, padx=10, pady=10)

        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        label3 = ttk.Label(self.root, text="Mức lương:")
        label3.grid(row=2, column=0, padx=10, pady=10)

        self.salary_entry = ttk.Entry(self.root)
        self.salary_entry.grid(row=2, column=1, padx=10, pady=10)

        label4 = ttk.Label(self.root, text="Mã phòng ban:")
        label4.grid(row=3, column=0, padx=10, pady=10)

        self.dept_id_entry = ttk.Entry(self.root)
        self.dept_id_entry.grid(row=3, column=1, padx=10, pady=10)

        label5 = ttk.Label(self.root, text="Tên phòng ban:")
        label5.grid(row=4, column=0, padx=10, pady=10)

        self.dept_name_entry = ttk.Entry(self.root)
        self.dept_name_entry.grid(row=4, column=1, padx=10, pady=10)

        # Tạo nút để thêm nhân viên
        add_button = ttk.Button(self.root, text="Thêm nhân viên", command=self.add_employee)
        add_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để liệt kê nhân viên
        list_button = ttk.Button(self.root, text="Liệt kê nhân viên", command=self.list_employees)
        list_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để lưu danh sách vào tập tin
        save_button = ttk.Button(self.root, text="Lưu vào tập tin", command=self.save_to_file)
        save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để chỉnh sửa nhân viên
        edit_button = ttk.Button(self.root, text="Chỉnh sửa nhân viên", command=self.open_edit_window)
        edit_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để mở cửa sổ xóa nhân viên
        remove_button = ttk.Button(self.root, text="Xóa nhân viên", command=self.open_remove_window)
        remove_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để mở cửa sổ tăng mức lương
        increase_salary_button = ttk.Button(self.root, text="Tăng lương", command=self.open_increase_salary_window)
        increase_salary_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        # Tạo nút để thoát
        exit_button = ttk.Button(self.root, text="Thoát", command=self.root.destroy)
        exit_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
    
    def add_employee(self):
        emp_id = self.emp_id_entry.get()
        name = self.name_entry.get()
        salary = self.salary_entry.get()
        dept_id = self.dept_id_entry.get()
        dept_name = self.dept_name_entry.get()

        if emp_id and name and salary and dept_id and dept_name:
            if emp_id in self.existing_emp_ids:
                messagebox.showerror("Lỗi", f"Mã số nhân viên {emp_id} đã tồn tại.")
            else:
                confirmation = messagebox.askyesno("Xác nhận thêm nhân viên", f"Xác nhận thêm nhân viên {name} (Mã số: {emp_id})?")
                if confirmation:
                    employee = Employee(emp_id, name, salary, dept_id, dept_name)
                    self.employees.append(employee)
                    self.existing_emp_ids.add(emp_id)  # Thêm mã nhân viên vào danh sách đã tồn tại
                    messagebox.showinfo("Thông báo", "Nhân viên đã được thêm vào danh sách.")
                    self.clear_entries()
        else:
            messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin nhân viên.")


    def clear_entries(self):
        self.emp_id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.salary_entry.delete(0, 'end')
        self.dept_id_entry.delete(0, 'end')
        self.dept_name_entry.delete(0, 'end')

    def list_employees(self):
        if not self.employees:
            messagebox.showinfo("Danh sách nhân viên", "Danh sách nhân viên rỗng.")
        else:
            employee_list = "Danh sách nhân viên:\n"
            for employee in self.employees:
                employee_list += f"Mã số: {employee.emp_id}, Họ tên: {employee.name}, Mức lương: {employee.salary}, Mã phòng ban: {employee.dept_id}, Tên phòng ban: {employee.dept_name}\n"
            messagebox.showinfo("Danh sách nhân viên", employee_list)
    
    def save_to_file(self):
        confirmation = messagebox.askyesno("Xác nhận lưu", "Xác nhận lưu danh sách nhân viên vào tập tin NV.txt?")
        if confirmation:
            with open('./NV.txt', 'w', encoding='utf-8') as file:
                for employee in self.employees:
                    file.write(f"{employee.emp_id};{employee.name};{employee.salary};{employee.dept_id};{employee.dept_name}\n")
            messagebox.showinfo("Thông báo", "Danh sách nhân viên đã được lưu vào tập tin NV.txt.")

    
    def open_remove_window(self):
        remove_window = Toplevel(self.root)
        remove_window.title("Xóa nhân viên")

        label = tk.Label(remove_window, text="Nhập mã số nhân viên cần xóa:")
        label.pack(padx=10, pady=10)

        emp_id_entry = tk.Entry(remove_window)
        emp_id_entry.pack(padx=10, pady=10)

        confirm_button = tk.Button(remove_window, text="Xác nhận", command=lambda: self.confirm_remove_employee(remove_window, emp_id_entry))
        confirm_button.pack(padx=10, pady=10)
        # Đặt con trỏ chuột vào ô nhập mã số
        emp_id_entry.focus_set()


    def confirm_remove_employee(self, remove_window, emp_id_entry):
        emp_id = emp_id_entry.get()
        remove_window.destroy()

        for employee in self.employees:
            if employee.emp_id == emp_id:
                confirmation = messagebox.askyesno("Xác nhận xóa nhân viên", f"Xác nhận xóa nhân viên {employee.name} (Mã số: {employee.emp_id}).")
                if confirmation:
                    self.employees.remove(employee)
                    messagebox.showinfo("Thông báo", f"Nhân viên {employee.name} đã bị loại bỏ.")
                    self.clear_entries()
                return
        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên với mã số này.")

    def open_increase_salary_window(self):
        increase_salary_window = Toplevel(self.root)
        increase_salary_window.title("Tăng mức lương")

        label = tk.Label(increase_salary_window, text="Nhập mã số nhân viên cần tăng lương:")
        label.pack(padx=10, pady=10)

        emp_id_entry = tk.Entry(increase_salary_window)
        emp_id_entry.pack(padx=10, pady=10)

        confirm_button = tk.Button(increase_salary_window, text="Xác nhận", command=lambda: self.confirm_increase_salary(increase_salary_window, emp_id_entry))
        confirm_button.pack(padx=10, pady=10)
        # Đặt con trỏ chuột vào ô nhập mã số
        emp_id_entry.focus_set()

    def confirm_increase_salary(self, increase_salary_window, emp_id_entry):
        emp_id = emp_id_entry.get()
        increase_salary_window.destroy()

        for employee in self.employees:
            if employee.emp_id == emp_id:
                current_salary = employee.salary
                confirmation = simpledialog.askstring("Xác nhận tăng lương", f"Xác nhận tăng lương cho nhân viên {employee.name} (Mức lương hiện tại: {current_salary}).\nNhập số tiền tăng lương:")
                if confirmation is not None:
                    try:
                        increase_amount = float(confirmation)
                        new_salary = float(current_salary) + increase_amount
                        employee.salary = new_salary
                        messagebox.showinfo("Thông báo", f"Mức lương của nhân viên {employee.name} đã được tăng lên {new_salary}.")
                        self.clear_entries()
                    except ValueError:
                        messagebox.showerror("Lỗi", "Vui lòng nhập một số hợp lệ để tăng mức lương.")
                return
        messagebox.showerror("Lỗi", "Không tìm thấy nhân viên với mã số này.")

    def open_edit_window(self):
        edit_window = Toplevel(self.root)
        edit_window.title("Chỉnh sửa thông tin nhân viên")

        label = tk.Label(edit_window, text="Chọn nhân viên để chỉnh sửa hoặc xóa:")
        label.pack(padx=10, pady=10)
        
        employee_buttons = []  # Danh sách các nút đại diện cho nhân viên
        for employee in self.employees:
            employee_button = tk.Button(edit_window, text=f"{employee.name} (Mã số: {employee.emp_id})", command=lambda e=employee: self.edit_or_remove_selected_employee(edit_window, e))
            employee_buttons.append(employee_button)
            employee_button.pack(padx=10, pady=5)

    def edit_or_remove_selected_employee(self, edit_window, selected_employee):
        edit_window.destroy()

        choice_window = Toplevel(self.root)
        choice_window.title("Chọn hành động")

        label = tk.Label(choice_window, text=f"Chọn hành động cho nhân viên {selected_employee.name} (Mã số: {selected_employee.emp_id}):")
        label.pack(padx=10, pady=10)

        edit_button = tk.Button(choice_window, text="Chỉnh sửa", command=lambda: self.edit_employee_details(choice_window, selected_employee))
        edit_button.pack(padx=10, pady=5)

        remove_button = tk.Button(choice_window, text="Xóa", command=lambda: self.confirm_remove_employee(choice_window, selected_employee))
        remove_button.pack(padx=10, pady=5)

    def edit_employee_details(self, choice_window, employee):
        choice_window.destroy()

        edit_window = Toplevel(self.root)
        edit_window.title("Chỉnh sửa thông tin nhân viên")

        label = tk.Label(edit_window, text="Chỉnh sửa thông tin cho nhân viên:")
        label.pack(padx=10, pady=10)

        label_emp_id = tk.Label(edit_window, text="Mã số:")
        label_emp_id.pack(padx=10, pady=5)

        emp_id_entry = tk.Entry(edit_window)
        emp_id_entry.insert(0, employee.emp_id)
        emp_id_entry.pack(padx=10, pady=5)

        label_name = tk.Label(edit_window, text="Họ tên:")
        label_name.pack(padx=10, pady=5)

        name_entry = tk.Entry(edit_window)
        name_entry.insert(0, employee.name)
        name_entry.pack(padx=10, pady=5)

        label_salary = tk.Label(edit_window, text="Mức lương:")
        label_salary.pack(padx=10, pady=5)

        salary_entry = tk.Entry(edit_window)
        salary_entry.insert(0, employee.salary)
        salary_entry.pack(padx=10, pady=5)

        label_dept_id = tk.Label(edit_window, text="Mã phòng ban:")
        label_dept_id.pack(padx=10, pady=5)

        dept_id_entry = tk.Entry(edit_window)
        dept_id_entry.insert(0, employee.dept_id)
        dept_id_entry.pack(padx=10, pady=5)

        label_dept_name = tk.Label(edit_window, text="Tên phòng ban:")
        label_dept_name.pack(padx=10, pady=5)

        dept_name_entry = tk.Entry(edit_window)
        dept_name_entry.insert(0, employee.dept_name)
        dept_name_entry.pack(padx=10, pady=5)

        # Đặt con trỏ chuột vào ô nhập họ tên
        name_entry.focus_set()
        edit_button = tk.Button(edit_window, text="Xác nhận chỉnh sửa", command=lambda: self.confirm_edit_employee_details(edit_window, employee, emp_id_entry, name_entry, salary_entry, dept_id_entry, dept_name_entry))
        edit_button.pack(padx=10, pady=10)

    def confirm_edit_employee_details(self, edit_window, employee, emp_id_entry, name_entry, salary_entry, dept_id_entry, dept_name_entry):
        new_emp_id = emp_id_entry.get()
        new_name = name_entry.get()
        new_salary = salary_entry.get()
        new_dept_id = dept_id_entry.get()
        new_dept_name = dept_name_entry.get()
        
        edit_window.destroy()

        confirmation = messagebox.askyesno("Xác nhận chỉnh sửa", f"Xác nhận chỉnh sửa thông tin cho nhân viên {new_name} (Mã số: {new_emp_id})?")
        if confirmation:
            employee.emp_id = new_emp_id
            employee.name = new_name
            employee.salary = new_salary
            employee.dept_id = new_dept_id
            employee.dept_name = new_dept_name
            messagebox.showinfo("Thông báo", "Thông tin nhân viên đã được chỉnh sửa.")


    def confirm_remove_employee(self, choice_window, employee):
        choice_window.destroy()

        confirmation_window = Toplevel(self.root)
        confirmation_window.title("Xác nhận xóa")

        label = tk.Label(confirmation_window, text=f"Xác nhận xóa nhân viên {employee.name} (Mã số: {employee.emp_id})?")
        label.pack(padx=10, pady=10)

        confirm_button = tk.Button(confirmation_window, text="Xác nhận xóa", command=lambda: self.remove_employee(confirmation_window, employee))
        confirm_button.pack(padx=10, pady=5)

    def remove_employee(self, confirmation_window, employee):
        confirmation_window.destroy()

        self.employees.remove(employee)
        self.existing_emp_ids.remove(employee.emp_id)
        messagebox.showinfo("Thông báo", f"Nhân viên {employee.name} đã bị loại bỏ.")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()
