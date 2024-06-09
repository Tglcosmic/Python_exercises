import numpy as np

#Tạo mảng 55 phần tử trong khoảng [-5.5, 55.5]
arr = np.linspace(-5.5, 55.5, 55)
# print(arr)

#Làm tròn đến 2 số thập phân
rounded_arr = np.around(arr, decimals=2)
# print(rounded_arr)

#Thay thế 7 giá trị không phải số (NAN) vào mảng ban đầu
nan_indices = np.random.choice(range(len(arr)), 7, replace=False)
rounded_arr[nan_indices] = np.nan
# print(rounded_arr)

#Thay đổi các giá trị mảng thành 0 nếu giá trị đó là âm
rounded_arr[rounded_arr < 0] = 0
# print(rounded_arr)

#Loại bỏ các phần tử NAN ra khỏi mảng
cleaned_arr = rounded_arr[~np.isnan(rounded_arr)]
# print(cleaned_arr)

#Dùng hàm để tạo ra mảng arr_2D có kích thước 6 hàng
arr_2D = cleaned_arr.reshape(6, -1)
# print(arr_2D)

#Tạo mảng arr_3D với yêu cầu 6 hàng 4 cột
arr_3D = cleaned_arr.reshape(-1, 6, 4)
# print(arr_3D)



