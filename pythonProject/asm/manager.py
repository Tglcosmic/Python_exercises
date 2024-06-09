import re


# Hàm để kiểm tra xem mã nhân viên có đúng theo cấu trúc [A-z]{2}[0-9]{5}
def validate_employee_id(emp_id):
    pattern = r'^[A-Z]{2}\d{5}$'
    return re.match(pattern, emp_id) is not None


# Hàm để kiểm tra xem mã nhân viên đã tồn tại trong danh sách hay chưa
def check_duplicate_id(emp_id):
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            existing_id = line.strip().split(',')[1]
            if existing_id == emp_id:
                return True
    return False


# Hàm để nhập thông tin của một nhân viên từ bàn phím
def input_employee_info():
    while True:
        while True:
            emp_type = input("Nhập loại nhân viên (1: hanhchinh, 2: tiepthi, 3: truongphong):").lower()
            if emp_type not in ['1', '2', '3', 'hanhchinh', 'tiepthi', 'truongphong']:
                print("Loại nhân viên không hợp lệ.")
                continue
        emp_id = input("Mã nhân viên: ")
        if not validate_employee_id(emp_id):
            print("Mã nhân viên không đúng định dạng. Vui lòng nhập lại.")
            continue
        if check_duplicate_id(emp_id):
            print("Mã nhân viên đã tồn tại. Vui lòng nhập lại.")
            continue
        break

    emp_name = input("Họ tên: ")
    emp_salary = float(input("Lương: "))
    if emp_type.lower() == 'tiếp thị':
        sales_volume = float(input("Doanh số bán hàng: "))
        commission_rate = float(input("Tỉ lệ hoa hồng (%): "))
        return (emp_type, emp_id, emp_name, emp_salary, sales_volume, commission_rate)
    elif emp_type.lower() == 'trưởng phòng':
        responsibility_salary = float(input("Lương trách nhiệm: "))
        return (emp_type, emp_id, emp_name, emp_salary, responsibility_salary)
    else:
        return (emp_type, emp_id, emp_name, emp_salary)

# Hàm để nhập danh sách nhân viên và lưu vào file
def input_employee_list():
    num_employees = int(input("Nhập số lượng nhân viên: "))
    with open("employees.txt", "a", encoding="utf-8") as file:
        for _ in range(num_employees):
            while True:
                emp_info = input_employee_info()
                emp_id = emp_info[1]
                if not check_duplicate_id(emp_id):
                    file.write(','.join(map(str, emp_info)) + '\n')
                    break
                else:
                    print("Mã nhân viên đã tồn tại. Vui lòng nhập lại.")


# Hàm để cập nhật thông tin nhân viên theo mã
def update_employee_by_id(emp_id):
    if not check_duplicate_id(emp_id):
        print("Không tìm thấy nhân viên có mã", emp_id)
        return
    delete_employee_by_id(emp_id)
    with open("employees.txt", "a", encoding="utf-8") as file:
        emp_info = input_employee_info()
        file.write(','.join(map(str, emp_info)) + '\n')
    print("Đã cập nhật thông tin cho nhân viên có mã", emp_id)


# Hàm để đọc danh sách nhân viên từ file và xuất ra màn hình
def read_employee_list():
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            emp_type = emp_info[0]
            emp_id = emp_info[1]
            emp_name = emp_info[2]
            if emp_type.lower() == 'tiếp thị':
                emp_salary = float(emp_info[3]) + float(emp_info[4]) * (float(emp_info[5]) / 100)
                print("{:<15}{:<10}{:<20}{:<20}".format(emp_type, emp_id, emp_name, emp_salary))
            elif emp_type.lower() == 'trưởng phòng':
                emp_salary = float(emp_info[3]) + float(emp_info[4])
                print("{:<15}{:<10}{:<20}{:<20}".format(emp_type, emp_id, emp_name, emp_salary))
            else:
                emp_salary = float(emp_info[3])
                print("{:<15}{:<10}{:<20}{:<20}".format(emp_type, emp_id, emp_name, emp_salary))

# Hàm để tìm nhân viên theo mã
def find_employee_by_id(emp_id):
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            if emp_info[1] == emp_id:
                print(emp_info)
                return
        print("Không tìm thấy nhân viên có mã", emp_id)


# Hàm để xóa nhân viên theo mã
def delete_employee_by_id(emp_id):
    with open("employees.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("employees.txt", "w", encoding="utf-8") as file:
        for line in lines:
            emp_info = line.strip().split(',')
            if emp_info[1] != emp_id:
                file.write(line)
    print("Đã xóa nhân viên có mã", emp_id)


# Hàm để tìm nhân viên theo khoảng lương
def find_employee_by_salary_range(min_salary, max_salary):
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            salary = float(emp_info[3])
            if min_salary <= salary <= max_salary:
                print(emp_info)


# Hàm để sắp xếp danh sách nhân viên theo họ và tên
def sort_employees_by_name():
    with open("employees.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines.sort(key=lambda x: x.strip().split(',')[2])  # Sắp xếp theo họ và tên
    with open("employees.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)

# Hàm để tính toán thu nhập của mỗi nhân viên
def calculate_income(emp_info):
    emp_type = emp_info[0].lower()
    if emp_type == 'tiếp thị':
        sales_volume, commission_rate = float(emp_info[4]), float(emp_info[5]) / 100
        return float(emp_info[3]) + sales_volume * commission_rate
    elif emp_type == 'trưởng phòng':
        return float(emp_info[3]) + float(emp_info[4])
    else:
        return float(emp_info[3])

# Hàm để sắp xếp danh sách nhân viên theo thu nhập
def sort_employees_by_income():
    with open("employees.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines.sort(key=lambda x: calculate_income(list(map(str.strip, x.split(',')))),
               reverse=True)  # Sắp xếp theo thu nhập
    with open("employees.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)


# Hàm để xuất 5 nhân viên có thu nhập cao nhất
def top_5_employees_by_income():
    with open("employees.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    sorted_lines = sorted(lines, key=lambda x: calculate_income(list(map(str.strip, x.split(',')))), reverse=True)
    print("Top 5 nhân viên có thu nhập cao nhất:")
    for line in sorted_lines[:5]:
        print(line.strip())
