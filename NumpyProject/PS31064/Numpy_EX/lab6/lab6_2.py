import numpy as np

# 1. Tạo mảng NumPy 2 chiều 4x3 từ 1 đến 12
arr_2d = np.arange(1, 13).reshape(4, 3)

# Tạo mảng NumPy 1 chiều với 3 phần tử từ 10 đến 30
arr_1d = np.arange(10, 31, 10)

# 2. Thực hiện phép cộng giữa mảng 2 chiều và mảng 1 chiều với broadcasting và in ra kết quả
result_broadcasting = arr_2d + arr_1d
print("Kết quả của phép cộng giữa mảng 2 chiều và mảng 1 chiều:\n", result_broadcasting)

# 3. Tính tổng các phần tử theo từng cột trong mảng 2 chiều và in ra kết quả
sum_columns = np.sum(arr_2d, axis=0)
print("Tổng các phần tử theo từng cột trong mảng 2 chiều:", sum_columns)

# 4. Tính tổng các phần tử theo từng hàng trong mảng 2 chiều và in ra kết quả
sum_rows = np.sum(arr_2d, axis=1)
print("Tổng các phần tử theo từng hàng trong mảng 2 chiều:", sum_rows)
