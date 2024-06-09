def show_menu(option):
    match option:
        case "1":
            print("Bạn đã chọn mục 1: Xem thông tin.")
        case "2":
            print("Bạn đã chọn mục 2: Chỉnh sửa dữ liệu.")
        case "3":
            print("Bạn đã chọn mục 3: Thoát chương trình.")
        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Hiển thị menu
print("----- Menu -----")
print("1. Xem thông tin")
print("2. Chỉnh sửa dữ liệu")
print("3. Thoát chương trình")

# Nhập lựa chọn từ người dùng
user_choice = input("Nhập lựa chọn của bạn (1-3): ")

# Gọi hàm show_menu để xử lý lựa chọn
show_menu(user_choice)
