class NhanVien:
    def __init__(self, ma_nv, ho_ten, luong_co_ban):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban

    def get_Thu_Nhap(self):
        return self.luong_co_ban

class TiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.doanh_so = doanh_so
        self.hoa_hong = hoa_hong

    def get_Thu_Nhap(self):
        return self.luong_co_ban + self.doanh_so * self.hoa_hong

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, phu_cap):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        self.phu_cap = phu_cap

    def get_Thu_Nhap(self):
        return self.luong_co_ban + self.phu_cap

def nhap_list_nv():
    list_nv = []
    while True:
        try:
            n =int(input("Nhập số lượng nhân viên: "))
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

            id = input("Nhập mã nhân viên: ")
            name = input("Nhập họ và tên: ")
            salary = float(input("Nhập lương cơ bản: "))

            if loai_nv == '1' or loai_nv == 'hanhchinh':
                nv = NhanVien(id, name, salary)
            elif loai_nv == '2' or loai_nv == 'tiepthi':
                sales = float(input("Nhập doanh số: "))
                commission = float(input("Nhập tỉ lệ hoa hồng: "))
                nv = TiepThi(id, name, salary, sales, commission)
            elif loai_nv == '3' or loai_nv == 'truongphong':
                allowance = float(input("Nhập phụ cấp: "))
                nv = TruongPhong(id, name, salary, allowance)

            list_nv.append(nv)
            break

    return list_nv

def tim_nv_theo_ma(list_nv, id):
    for nv in list_nv:
        if nv.ma_nv == id:
            return nv
    return None

def xoa_nv_theo_ma(list_nv, id):
    for nv in list_nv:
        if nv.ma_nv == id:
            list_nv.remove(nv)
            return True
    return False

def cap_nhat_nv_theo_ma(list_nv, id):
    for nv in list_nv:
        if nv.ma_nv == id:
            new_salary = float(input("Nhập lương mới: "))
            nv.luong_co_ban = new_salary
            return True
    return False

def find_nv_theo_khoang_luong(list_nv, luong_min, luong_max):
    list_kq = []
    for nv in list_nv:
        if luong_min <= nv.get_Thu_Nhap() <= luong_max:
            list_kq.append(nv)
    return list_kq

def sorted_nv_theo_ten(list_nv):
    return sorted(list_nv, key=lambda nv: nv.ho_ten)

def sorted_theo_thu_nhap(list_nv):
    return sorted(list_nv, key=lambda nv: nv.get_Thu_Nhap())

def xuat_top_5_nv_cao_nhat(list_nv):
    top_5_nv = sorted(list_nv, key=lambda nv: nv.get_Thu_Nhap(), reverse=True)[:5]
    for i, nv in enumerate(top_5_nv, 1):
        print(f"Top {i}: {nv.ho_ten} - Thu Nhập: {nv.get_Thu_Nhap()}")

def xuat_list_nv(list_nv):
    for nv in list_nv:
        print("Mã NV:", nv.ma_nv)
        print("Họ và Tên:", nv.ho_ten)
        print("Thu nhập:", nv.get_Thu_Nhap())

def menu():
    list_nv = []

    while True:
        print("╔═════════════════════════════════════════╗")
        print("║                   MENU                  ║")
        print("╟─────────────────────────────────────────╢")
        print("║ 1. Nhập danh sách nhân viên             ║")
        print("║ 2. Xuất danh sách nhân viên             ║")
        print("║ 3. Tìm nhân viên theo mã                ║")
        print("║ 4. Xóa nhân viên theo mã                ║")
        print("║ 5. Cập nhật nhân viên theo mã           ║")
        print("║ 6. Tìm nhân viên theo khoảng lương      ║")
        print("║ 7. Sắp xếp nhân viên theo họ tên        ║")
        print("║ 8. Sắp xếp nhân viên theo thu nhập      ║")
        print("║ 9. Xuất 5 nhân viên thu nhập cao nhất   ║")
        print("║ 0. Exit                                 ║")
        print("╚═════════════════════════════════════════╝")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            list_nv = nhap_list_nv()
        elif choice == '2':
            xuat_list_nv(list_nv)
        elif choice == '3':
            id = input("Nhập mã nhân viên cần tìm: ")
            nv = tim_nv_theo_ma(list_nv, id)
            if nv:
                print("Thông tin Nhân viên: ")
                print("Mã nhân viên:", nv.ma_nv)
                print("Họ và tên:", nv.ho_ten)
                print("Thu nhập:", nv.get_Thu_Nhap())
            else:
                print("Không tìm thấy nhân viên có mã", id)
        elif choice == '4':
            id = input("Nhập mã nhân viên cần xóa: ")
            if xoa_nv_theo_ma(list_nv, id):
                print("Xóa nhân viên thành công!")
            else:
                print("Không tìm thấy nhân viên có mã", id)
        elif choice == '5':
            id = input("Nhập mã nhân viên cần cập nhật: ")
            if cap_nhat_nv_theo_ma(list_nv, id):
                print("Cập nhật thông tin nhân viên thành công!")
            else:
                print("Không tìm thấy nhân viên có mã", id)
        elif choice == '6':
            luong_min = float(input("Nhập thu nhập tối thiểu: "))
            luong_max = float(input("Nhập thu nhập tối đa: "))
            danh_sach_kq = find_nv_theo_khoang_luong(list_nv, luong_min, luong_max)
            print("Nhân viên trong khoảng thu nhập từ", luong_min, "đến", luong_max)
            for nv in danh_sach_kq:
                print("Mã NV:", nv.ma_nv)
                print("Họ và Tên:", nv.ho_ten)
                print("Thu nhập:", nv.get_Thu_Nhap())
        elif choice == '7':
            list_nv = sorted_nv_theo_ten(list_nv)
            xuat_list_nv(list_nv)
        elif choice == '8':
            list_nv = sorted_theo_thu_nhap(list_nv)
            xuat_list_nv(list_nv)
        elif choice == '9':
            xuat_top_5_nv_cao_nhat(list_nv)
        elif choice == '0':
            break

menu()
