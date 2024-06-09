from quan_ly import *

def menu():
    filename = "employees.txt"
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
            ghi_vao_file(list_nv, filename)
        elif choice == '2':
            print("{:<8}{:<16}{:<16}".format("ID", "Tên Nhân Viên", "Tổng Lương"))
            xuat_list_nv(filename)
        elif choice == '3':
            id = input("Nhập mã nhân viên cần tìm: ")
            print("{:<8}{:<16}{:<16}".format("ID", "Tên Nhân Viên", "Tổng Lương"))
            tim_nv_theo_ma(id, filename)
        elif choice == '4':
            id = input("Nhập mã nhân viên cần xóa: ")
            xoa_nv_theo_ma(id, filename)
        elif choice == '5':
            id = input("Nhập mã nhân viên cần cập nhật: ")
            cap_nhat_nv_theo_ma(id, filename)
        elif choice == '6':
            min_salary = float(input("Nhập lương tối thiểu: "))
            max_salary = float(input("Nhập lương tối đa: "))
            print("{:<8}{:<16}{:<16}".format("ID", "Tên Nhân Viên", "Tổng Lương"))
            find_nv_theo_khoang_luong(min_salary, max_salary)
        elif choice == '7':
            sorted_nv_theo_ten(filename)
            print("Đã sắp xếp thành công")
            print("{:<8}{:<16}{:<16}".format("ID", "Tên Nhân Viên", "Tổng Lương"))
            xuat_list_nv(filename)
        elif choice == '8':
            sorted_theo_thu_nhap(filename)
            print("Đã sắp xếp thành công")
            print("{:<8}{:<16}{:<16}".format("ID", "Tên Nhân Viên", "Tổng Lương"))
            xuat_list_nv(filename)
        elif choice == '9':
            top_5_nv = top_5_nv_cao_nhat("employees.txt")
            print("{:<4}{:<8}{:<16}{:<16}".format("TOP", "ID", "Tên Nhân Viên", "Tổng Lương"))
            for i, nv in enumerate(top_5_nv, 1):
                print("{:<4}{:<8}{:<16}{:<16}".format(i, nv.id, nv.name, nv.get_Thu_Nhap()))
        elif choice == '0':
            break

menu()