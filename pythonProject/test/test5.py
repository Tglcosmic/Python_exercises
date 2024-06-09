## 1. xây dưng class ban đầu
# xây dựng lớp sinh viên
class SinhVien:
    # Thuộc tính Sinh vien
    massv = ""
    tensv = ""
    diem_tb = ""

    # Phương thức của lớp sinh viên

    def xuatthongtin_sv(self):
        print("Thông tin sinh viên: ")
        print("Mã số sinh viên:", self.massv)
        print("Mã số sinh viên:", self.tensv)
        print("Mã số sinh viên:", self.diem_tb)


# Tạo một đối tượng cho lớp sinh viên
sv1 = SinhVien()
# Gián các giátri5i dữ liệu cho các thuộc tính
sv1.massv = "ps001"
sv1.tensv = "Huỳnh Yến"
sv1.diem_tb = 8
# gọi phuong thức xuất thông tin sinh viên
sv1.xuatthongtin_sv()


# 2.sử dụng hàm init để khởi tạo các thuộc tính


class SinhVien:
    # Thuộc tính Sinh vien
    # massv = ""
    # tensv = ""
    # diem_tb = ""
    def __init__(self, masv, ten, diem):
        self.massv = masv
        self.tensv = ten
        self.diem_tb = diem

    # Phương thức của lớp sinh viên

    def xuatthongtin_sv(self):
        print("Thông tin sinh viên: ")
        print("Mã số sinh viên:", self.massv)
        print("Tên sinh vien sinh viên:", self.tensv)
        print("Điểm số sinh viên:", self.diem_tb)


# Tạo một đối tượng cho lớp sinh viên

# khởi tạo không cần nhập
# sv1 = SinhVien("ps001","Huynh Yến", 8)
# sv1.xuatthongtin_sv()

# khởi tạo và nhập thông tin từ bàn phím
masv = input("Nhập ma so sinh vien:")
ten = input("tên sinh viên:")
diem = int(input("nhap diem "))
sv2 = SinhVien(masv, ten, diem)
sv2.xuatthongtin_sv()


# 3. sử dụng hàm init,nhap, xuat
class SinhVien:
    # Thuộc tính Sinh vien
    massv = ""
    tensv = ""
    diem_tb = ""

    # Phương thức của lớp sinh viên
    def nhapthongtinsv(self):
        self.massv = input("Nhap ma so sinh vien")
        self.tensv = input("Nhap Ten sinh vien")
        self.diem_tb = float(input("Nhap diem"))

    def xuatthongtin_sv(self):
        print("Thông tin sinh viên: ")
        print("Mã số sinh viên:", self.massv)
        print("Tên sinh viên:", self.tensv)
        print("Điểm sinh viên:", self.diem_tb)


# # Tạo một đối tượng cho lớp sinh viên
# sv1 = SinhVien()
# # Gián các giátri5i dữ liệu cho các thuộc tính
# sv1.massv = "ps001"
# sv1.tensv = "Huỳnh Yến"
# sv1.diem_tb = 8
# # gọi phuong thức xuất thông tin sinh viên
# sv1.xuatthongtin_sv()
#  khỏi tạo và gọi hàm nhập xuất

sv3 = SinhVien()
sv3.nhapthongtinsv()
sv3.xuatthongtin_sv()