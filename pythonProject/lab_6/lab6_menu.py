import lab6_4
def menu():
    print("╔═════════════════════════════════════════╗")
    print("║               MENU                      ║")
    print("╟─────────────────────────────────────────╢")
    print("║ 1. Nhập danh sách sinh viên             ║")
    print("║ 2. Xuất thông tin danh sách sinh viên   ║")
    print("║ 3. Xuất danh sách sinh viên có học lực  ║")
    print("║    giỏi                                 ║")
    print("║ 4. Sắp xếp danh sách sinh viên theo     ║")
    print("║    điểm                                 ║")
    print("║ 5. Kết thúc                             ║")
    print("╚═════════════════════════════════════════╝")

while True:
    menu()
    chon = input("Chọn chức năng (1-5): ")

    if chon == "1":
        danh_sach_sinh_vien = lab6_4.nhap_danh_sach_sinh_vien()
    elif chon == "2":
        lab6_4.xuat_thong_tin_sinh_vien(danh_sach_sinh_vien)
    elif chon == "3":
        lab6_4.xuat_danh_sach_sinh_vien_hoc_luc_gioi(danh_sach_sinh_vien)
    elif chon == "4":
        lab6_4.sap_xep_danh_sach_sinh_vien_theo_diem(danh_sach_sinh_vien)
        lab6_4.xuat_thong_tin_sinh_vien(danh_sach_sinh_vien)
    elif chon == "5":
        print("Kết thúc chương trình.")
        break
    else:
        print("Chức năng không hợp lệ. Vui lòng chọn lại.")