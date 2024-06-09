from manager import *
# Main function
def main():
    while True:
        print("\n------ Quản lý nhân sự công ty Rồng Việt ------")
        print("1. Nhập danh sách nhân viên")
        print("2. Đọc danh sách nhân viên")
        print("3. Tìm nhân viên theo mã")
        print("4. Xóa nhân viên theo mã")
        print("5. Cập nhật thông tin nhân viên theo mã")
        print("6. Tìm nhân viên theo khoảng lương")
        print("7. Sắp xếp nhân viên theo họ tên")
        print("8. Sắp xếp nhân viên theo thu nhập")
        print("9. Xuất 5 nhân viên có thu nhập cao nhất")
        print("0. Thoát chương trình")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            input_employee_list()
        elif choice == '2':
            print("{:<15}{:<10}{:<20}{:<20}".format("loại NV","ID NV","Tên NV","Tổng Lương"))
            read_employee_list()
        elif choice == '3':
            emp_id = input("Nhập mã nhân viên cần tìm: ")
            find_employee_by_id(emp_id)
        elif choice == '4':
            emp_id = input("Nhập mã nhân viên cần xóa: ")
            delete_employee_by_id(emp_id)
        elif choice == '5':
            emp_id = input("Nhập mã nhân viên cần cập nhật: ")
            update_employee_by_id(emp_id)
        elif choice == '6':
            min_salary = float(input("Nhập lương tối thiểu: "))
            max_salary = float(input("Nhập lương tối đa: "))
            find_employee_by_salary_range(min_salary, max_salary)
        elif choice == '7':
            sort_employees_by_name()
        elif choice == '8':
            sort_employees_by_income()
        elif choice == '9':
            top_5_employees_by_income()
        elif choice == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()