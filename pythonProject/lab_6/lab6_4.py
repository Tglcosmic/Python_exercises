from lab6_2_6_3 import SinhVienIT, SinhVienBiz

def nhap_danh_sach_sinh_vien():
    danh_sach = []
    so_luong_sv = int(input("Nhập số lượng sinh viên: "))

    for i in range(so_luong_sv):
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        ho_ten = input("Họ tên: ")
        nganh = input("Ngành: ")
        loai_sv = input("Loại sinh viên (IT/Biz): ")

        if loai_sv == "IT":
            diem_java = float(input("Điểm Java: "))
            diem_html = float(input("Điểm HTML: "))
            diem_css = float(input("Điểm CSS: "))
            sv = SinhVienIT(ho_ten, nganh, diem_java, diem_html, diem_css)
        elif loai_sv == "Biz":
            diem_mkt = float(input("Điểm Marketing: "))
            diem_sales = float(input("Điểm Sales: "))
            sv = SinhVienBiz(ho_ten, nganh, diem_mkt, diem_sales)
        else:
            print("Loại sinh viên không hợp lệ. Vui lòng nhập lại.")
            continue

        danh_sach.append(sv)

    return danh_sach

def xuat_thong_tin_sinh_vien(danh_sach):
    print("\nThông tin danh sách sinh viên:")
    print("{:16}{:16}{:8}{:8}".format("Họ tên","Ngành","Điểm","Học Lực"))
    for sv in danh_sach:
        sv.xuat()

def xuat_danh_sach_sinh_vien_hoc_luc_gioi(danh_sach):
    print("\nDanh sách sinh viên có học lực giỏi:")
    for sv in danh_sach:
        if sv.get_hoc_luc() == "Giỏi":
            sv.xuat()
def sap_xep_danh_sach_sinh_vien_theo_diem(danh_sach):
    danh_sach.sort(key=lambda sv: sv.get_diem(), reverse=True)

