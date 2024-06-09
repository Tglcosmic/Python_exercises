import numpy as np

# Tạo một mảng NumPy 2 chiều có kích thước 4x4 với dữ liệu là số nguyên từ 0 đến 15.
arr_2d = np.random.randint(0, 15, [4, 4])
print(arr_2d)

# Sử dụng chỉ mục để truy cập phần tử ở hàng thứ 2 và cột thứ 3
print(f"Phần tử hàng thứ 2 và cột thứ 3 là: {arr_2d[1, 2]}")

# Thay đổi giá trị của phần tử này thành 100
arr_2d[1, 2] = 100
print(f"Phần tử đã thay đổi thành 100 là {arr_2d}")

# Tính và in ra tổng các phần tử trong hàng thứ 2 và tổng các phần tử trong cột thứ 3
print("Tổng các phần tử trong hàng thứ 2:", np.sum(arr_2d[1, :]))
print("Tổng các phần tử trong cột thứ 3:", np.sum(arr_2d[:, 2]))

# Tính tổng các phần tử theo từng hàng và từng cột trong mảng và in ra kết quả
print("Tổng các phần tử theo từng hàng:", np.sum(arr_2d, axis=1))
print("Tổng các phần tử theo từng cột:", np.sum(arr_2d, axis=0))