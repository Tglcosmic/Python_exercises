#pascalCase
class SinhVien:
# class sinhVienUdpm camelCase
    # Thuộc tính
    mssv = ""
    tensv = ""
    diemtb = ""
    # Phương thức
    def NhapInf(self):
        print("--Nhap thong tin sing vien-- ")
        self.tensv = input("Nhap ten sinh vien: ")
        self.mssv = input("Nhap mssv: ")
        self.diemtb = input("nhap diem sinh vien: ")
    def Xuat(self):
        print("Thông tin của sinh viên: ")
        print("Mã số sinh viên:", self.mssv)
        print("Tên sinh viên:", self.tensv)
        print("Điểm:", self.diemtb)
# sv1 = SinhVien()
# sv1.mssv = input("Nhập mã số sinh viên: ")
# sv1.tensv = input("Nhập tên sinh viên: ")
# sv1.diemtb = input("Nhập điểm của sinh viên: ")
# sv1.xuat()

sv2 = SinhVien()
sv2.NhapInf()
sv2.Xuat()