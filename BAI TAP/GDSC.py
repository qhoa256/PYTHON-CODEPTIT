from datetime import *

def start_end_of_week(week_number, year):
    # Tạo một đối tượng datetime cho ngày đầu tiên của năm
    first_day_of_year = datetime(year, 1, 1)

    # Tìm ngày đầu tiên của tuần 1 (thứ 2 đầu tiên trong năm)
    days_until_first_week = (8 - first_day_of_year.weekday()) % 7
    first_week_start = first_day_of_year + timedelta(days=days_until_first_week)

    # Tính ngày bắt đầu và kết thúc của tuần được chỉ định
    start_of_week = first_week_start + timedelta(weeks=(week_number - 1))
    end_of_week = start_of_week + timedelta(days=6)

    # Định dạng và in ra kết quả
    start_str = start_of_week.strftime("%d/%m/%Y")
    end_str = end_of_week.strftime("%d/%m/%Y")

    print(f"Tuần {week_number} của năm {year}: {start_str} - {end_str}")

# Sử dụng hàm
week_number = 3
year = 2023
start_end_of_week(week_number, year)
