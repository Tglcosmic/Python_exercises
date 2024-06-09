from class_nv import NhanVien, TiepThi, TruongPhong
import re

def tao_ma_id():
    try:
        with open("max_id.txt", "r", encoding="utf-8") as file:
            current_id = int(file.read())
    except FileNotFoundError:
        current_id = 0

    max_ma_id = current_id
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            ma_id = line.strip().split(',')[0]
            if ma_id.startswith("PS") and ma_id[2:].isdigit():
                ma_id = int(ma_id[2:])
                if ma_id > max_ma_id:
                    max_ma_id = ma_id

    with open("max_id.txt", "w", encoding="utf-8") as file:
        file.write(str(max_ma_id + 1))

    return f"PS{max_ma_id + 1:05d}"

def check_salary(salary):
    pattern = "^[A-Z][a-z]+$"
    return re.match(pattern, str(salary)) is None

def check_duplicate_id(emp_id):
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            existing_id = line.strip().split(',')[0]
            if existing_id == emp_id:
                return True
    return False
def nhap_list_nv():
    global nv
    list_nv = []
    while True:
        try:
            n = int(input("Nhập số lượng nhân viên: "))
            if n <= 0:
                raise ValueError("Số lượng nhân viên phải là số nguyên dương")
            break
        except ValueError as e:
            print("ERROR:", e)
    for i in range(n):
        while True:
            loai_nv = input("Nhập loại nhân viên (1: hanhchinh, 2: tiepthi, 3: truongphong):").lower()
            if loai_nv not in ['1', '2', '3', 'hanhchinh', 'tiepthi', 'truongphong']:
                print("Loại nhân viên không hợp lệ.")
                continue

            id = tao_ma_id()
            name = input("Nhập họ và tên: ")
            salary = float(input("Nhập lương cơ bản: "))
            if not check_salary(salary) or salary < 0:
                print("lương không đúng định dạng. Vui lòng nhập lại.")
                continue
            if loai_nv == '1' or loai_nv == 'hanhchinh':
                nv = NhanVien(id, name, salary)
            elif loai_nv == '2' or loai_nv == 'tiepthi':
                sales = float(input("Nhập doanh số: "))
                commission = float(input("Nhập tỉ lệ hoa hồng: "))
                nv = TiepThi(id, name, salary, sales, commission)
            elif loai_nv == '3' or loai_nv == 'truongphong':
                allownce = float(input("Nhập phụ cấp: "))
                nv = TruongPhong(id, name, salary, allownce)

            list_nv.append(nv)
            break

    return list_nv
def ghi_vao_file(list_nv, filename):
    with open(filename, 'a', encoding="utf-8") as file:
        for nv in list_nv:
            file.write("{},{},{}\n".format(nv.id, nv.name, nv.get_Thu_Nhap()))

def xuat_list_nv(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            print("{:<8}{:<16}{:<16}".format(emp_info[0], emp_info[1], emp_info[2]))
def tim_nv_theo_ma(id, filename):
    found = False
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            if emp_info[0] == id:
                print("{:<8}{:<16}{:<16}".format(emp_info[0], emp_info[1], emp_info[2]))
                found = True
                break
    if not found:
        print("Không tìm thấy nhân viên có mã", id)

def xoa_nv_theo_ma(id, filename):
    found = False  # Biến cờ để theo dõi xem đã tìm thấy mã nhân viên hay chưa
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            emp_info = line.strip().split(',')
            if emp_info[0] != id:
                file.write(line)
            else:
                found = True  # Đặt biến cờ thành True nếu tìm thấy mã nhân viên
    if found:
        print("Đã xóa nhân viên có mã", id)
    else:
        print("Không tìm thấy nhân viên có mã", id)  # Thông báo lỗi khi không tìm thấy mã

def cap_nhat_nv_theo_ma(emp_id, filename):
    if not check_duplicate_id(emp_id):
        print("Không tìm thấy nhân viên có mã", emp_id)
        return
    xoa_nv_theo_ma(emp_id, filename)
    with open(filename, "a", encoding="utf-8") as file:
        list_nv = nhap_list_nv()
        ghi_vao_file(list_nv, filename)
    print("Đã cập nhật thông tin cho nhân viên có mã", emp_id)

def find_nv_theo_khoang_luong(min_salary, max_salary):
    with open("employees.txt", "r", encoding="utf-8") as file:
        for line in file:
            emp_info = line.strip().split(',')
            salary = float(emp_info[2])
            if min_salary <= salary <= max_salary:
                emp_info = line.strip().split(',')
                print("{:<8}{:<16}{:<16}".format(emp_info[0], emp_info[1], emp_info[2]))

def sorted_nv_theo_ten(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines.sort(key=lambda x: x.strip().split(',')[1])  # Sắp xếp theo họ và tên
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)


def sorted_theo_thu_nhap(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    lines.sort(key=lambda x: x.strip().split(',')[2],reverse=True)  # Sắp xếp theo họ và tên
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)

def xuat_top_5_nv_cao_nhat(filename):
    danh_sach_nv = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            emp_info = line.strip().split(',')
            nv = NhanVien(emp_info[0], emp_info[1], float(emp_info[2]))
            danh_sach_nv.append(nv)
    return danh_sach_nv


def top_5_nv_cao_nhat(filename):
    danh_sach_nv = xuat_top_5_nv_cao_nhat(filename)
    sorted_nv = sorted(danh_sach_nv, key=lambda nv: nv.get_Thu_Nhap(), reverse=True)
    return sorted_nv[:5]
