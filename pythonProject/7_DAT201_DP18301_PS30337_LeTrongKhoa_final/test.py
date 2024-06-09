import asm2
import csv
class QuanLyNhanVien:
    def __init__(self):
        self.danhsachnv = []
    def nhap_nv(self):
        ma = int(input("Nhập mã nv: "))
        hoten = input("Nhập họ tên nv: ")
        luong = float(input("Nhập lương nv: "))
        phongban = input("Nhập vị trí phòng ban ( Trưởng Phòng ( TP ) // Tiếp thị ( TT ) ):")
        if phongban.lower() == 'tp':
            luongtn = float(input("Nhập lương trách nhiệm"))
            nv = asm2.TruongPhong(hoten, luong, ma, luongtn)
            self.danhsachnv.append(nv)
        elif phongban.lower() == 'tt':
            hh = float(input("Nhập tỉ lệ hoa hồng: "))
            ds = int(input("Nhập doanh số: "))
            nv = asm2.TiepThi(hoten, luong, ma, ds, hh)
            self.danhsachnv.append(nv)
        else:
            print("Chỉ nhập trưởng phòng hoặc tiếp thị.")
    def nhap_vao_file(self, file_nhap):
        with open(file_nhap,"a",newline = "", encoding="utf") as file:
            write = csv.writer(file)
            for nhanvien in self.danhsachnv:
                write.writerow([nhanvien.ma, nhanvien.hoten, nhanvien.get_thu_nhap(), nhanvien.get_thue()])
        file.close()
    def xuat_ds_nhanvien(self,file_nhap):
        print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            for line in read:
                ma, hoten, luong, thue = line
                print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
        file.close()
    def tim_nhan_vien(self,file_nhap):
        id = input("Nhập mã nhân viên cần tìm: ")
        found = False
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            for line in read:
                ma, hoten, luong, thue = line
                if ma == id:
                    print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
                    print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
                    found = True
                    break
            if not found:
                print("Không tìm thấy nhân viên")
        file.close()
    def tim_luong_nhan_vien(self, file_nhap):
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            while True:
                luongtt = float(input("Nhập lương tối thiểu cần tìm :"))
                luongtd = float(input("Nhập lương tối đa cần tìm: "))
                if luongtt < 0 or luongtt < luongtd or luongtd < 0:
                    break
                else:
                    print("Lương tối thiểu không hợp lệ")
            print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
            for line in read:
                ma, hoten, luong, thue = line
                if float(luong) >= luongtt and float(luong) <= luongtd :
                    print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
    def sap_xep_nv_hoten(self, file_nhap):
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            danh_sach = [line for line in read]
            danh_sach.sort(key= lambda x: x[1], reverse= True)
            print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
            for line in danh_sach:
                ma, hoten, luong, thue = line
                print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
    def sap_xep_nv_thunhap(self, file_nhap):
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            danh_sach = [line for line in read]
            danh_sach.sort(key= lambda x: float(x[2]))
            print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
            for line in danh_sach:
                ma, hoten, luong, thue = line
                print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
    def sap_xep_nv_thunhap_top5(self, file_nhap):
        with open(file_nhap,"r", encoding="utf") as file:
            read = csv.reader(file)
            next(read)
            danh_sach = [line for line in read]
            danh_sach.sort(key= lambda x: float(x[2]))
            print("{:<8} {:<16}{:<8}{:<8}".format("Mã", "Tên nhân viên", "Lương", "Thuế thu nhập"))
            count = 0
            for line in danh_sach:
                if count == 5:
                    break
                else:
                    ma, hoten, luong, thue = line
                    print("{:<8} {:<16}{:<8}{:<8}".format(ma, hoten, luong, thue))
                    count += 1
