import test
qlnv = test.QuanLyNhanVien()
def menu():
    print("""
            *.....................Menu................*   
            0. Thoát.                          
            1. Nhập danh sách nhân viên.            
            2. Danh sách nhân viên.                      
            3. Tìm nhân viên.                    
            4. Xóa nhân viên.                      
            5. Thay đổi/Cập nhật thông tin nhân viên.
            6. Tìm nhân viên theo mức lương.               
            7. Sắp xếp nhân viên.   
            8. Sắp xếp nhân viên theo thu nhập.      
            9. 5 nhân viên có mức lương cao nhất.  
            *.........................................*
""")
stt = 1
option = 1
menu()
ten_file = "danh_sach_nhanvien.csv"
while option != 0:
    option = input("-----Lựa chọn chức năng chương trình-----: ")
    if option.isdigit():
        option = int(option)
        match option:
            case 0:
                print("Đã kết thúc chương trình: ")
                break
            case 1:
                n = int(input("Nhập số nhân viên"))
                for stt in range(stt, n + stt):
                    stt += 1
                    qlnv.nhap_nv()
                qlnv.nhap_vao_file(ten_file)
            case 2:
                qlnv.xuat_ds_nhanvien(ten_file)
            case 3:
                qlnv.tim_nhan_vien(ten_file)
            case 4:
                print("4. Xóa nhân viên")
            case 5:
                print("5. Thay đổi/Cập nhật thông tin nhân viên")
            case 6:
                qlnv.tim_luong_nhan_vien(ten_file)
            case 7:
                qlnv.sap_xep_nv_hoten(ten_file)
            case 8:
                qlnv.sap_xep_nv_thunhap(ten_file)
            case 9:
                qlnv.sap_xep_nv_thunhap_top5(ten_file)
            case _:
                print("Chức năng không hợp lệ vui lòng nhập lại")
    else:
        print("lỗi")