import numpy as np

# 1. Tạo mảng arr_1D thập phân gồm 36 phần tử ngẫu nhiên trong khoảng 1 – 25
arr_1D = np.linspace(1 ,25, 36)
# print(arr_1D)

# 2. Dùng hàm để tạo ra mảng arr_2D có kích thước 6 hàng (số cột hệ thống tự tính) từ mảng arr_1D ban đầu
arr_2D = arr_1D.reshape(6, -1)
# print(arr_2D)

# 3. Tạo mảng arr_3D với yêu cầu 3 hàng, 3 cột (số lớp hệ thống tự tính) từ mảng arr_1D ban đầu
arr_3D = arr_1D.reshape(-1, 3, 3)
# print(arr_3D)

# 4. Viết chương trình in ra:
#  Các giá trị trong mảng
#  Số lượng phần tử có trong mảng.
#  Hình dạng của mảng
print(f"mảng arr_1D:\n{arr_1D}\nSố lượng phần tử: {np.size(arr_1D)}\nHình dạng của mảng: {np.shape(arr_1D)}\n")
print(f"mảng arr_1D:\n{arr_2D}\nSố lượng phần tử: {np.size(arr_2D)}\nHình dạng của mảng: {np.shape(arr_2D)}\n")
print(f"mảng arr_1D:\n{arr_3D}\nSố lượng phần tử: {np.size(arr_3D)}\nHình dạng của mảng: {np.shape(arr_3D)}\n")