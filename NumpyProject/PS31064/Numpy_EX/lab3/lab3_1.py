import numpy as np
# Tạo một mảng NumPy để lưu trữ danh sách sản phẩm ban đầu
product_list = np.array(["Máy giặt", "Tủ lạnh", "Lò vi sóng", "Điện thoại", "Máy tính bảng"])

def add_product(product):
    global product_list
    # Hoàn thiện hàm THÊM sau
    product_list = np.append(product_list, product)
    print(f"Sản phẩm '{product}' đã được thêm vào danh sách.")
def delete_product(index_or_name):
    global product_list
    try:
        index_or_name = int(index_or_name)
        if index_or_name >= 0 and index_or_name < len(product_list):
            deleted_product = product_list[index_or_name]
            # Hoàn thiện hàm XÓA sau
            product_list = np.delete(product_list, index_or_name)
            print(f"Sản phẩm '{deleted_product}' đã bị xóa khỏi danh sách.")
        else:
            print("Chỉ mục không hợp lệ.")
    except ValueError:
        if index_or_name in product_list:
            index = np.where(product_list == index_or_name)
            deleted_product = product_list[index[0][0]]
            # Hoàn thiện hàm XÓA sau
            product_list = np.delete(product_list, index[0][0])
            print(f"Sản phẩm '{deleted_product}' đã bị xóa khỏi danh sách.")
        else:
            print("Sản phẩm không tồn tại trong danh sách.")
def display_product_list():
    print("Danh sách sản phẩm:")
    for idx, product in enumerate(product_list):
        print(f"{idx}. {product}")
# Menu chương trình
while True:
 print("\n------ MENU ------")
 print("1. Thêm sản phẩm")
 print("2. Xóa sản phẩm")
 print("3. Hiển thị danh sách sản phẩm")
 print("4. Thoát")
 choice = input("Chọn chức năng (1-4): ")
 if choice == '1':
    new_product = input("Nhập tên sản phẩm mới: ")
    add_product(new_product)
 elif choice == '2':
    index_or_name = input("Nhập chỉ mục hoặc tên sản phẩm cần xóa: ")
    delete_product(index_or_name)
 elif choice == '3':
    display_product_list()
 elif choice == '4':
    print("Kết thúc chương trình.")
    break
 else:
    print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 4.")
