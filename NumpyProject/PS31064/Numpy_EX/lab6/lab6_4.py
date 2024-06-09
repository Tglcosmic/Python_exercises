import numpy as np

# Tạo một mảng NumPy 2 chiều 4x5 từ 1 đến 20
arr_2d = np.arange(1, 21).reshape(4, 5)
print("mảng gốc:\n", arr_2d)

# 1. Thực hiện cắt lát mảng để lấy một phần mảng từ hàng thứ 2 đến hàng thứ 3 và từ cột thứ 1 đến cột thứ 3
sliced_arr = arr_2d[1:3, 0:3]
print("Phần mảng sau khi cắt lát:\n", sliced_arr)

# 2. Tạo một mảng mới 1 chiều từ mảng ban đầu bằng cách làm phẳng mảng và in ra kết quả
arr_1d = arr_2d.flatten()
print("Mảng mới 1 chiều từ mảng ban đầu:\n", arr_1d)

# 3. Sắp xếp mảng mới theo thứ tự giảm dần và in ra kết quả
arr_1d_sorted = np.sort(arr_1d)[::-1]
print("Mảng mới sau khi sắp xếp giảm dần:\n", arr_1d_sorted)

# 4. Tính và in ra tổng các phần tử trong mảng mới
sum_elements = np.sum(arr_1d)
print("Tổng các phần tử trong mảng mới:", sum_elements)
