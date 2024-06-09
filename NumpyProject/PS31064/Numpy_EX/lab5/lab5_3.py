import numpy as np

# Tạo một mảng NumPy 2 chiều có kích thước 5x5 với dữ liệu số nguyên từ 1 đến 25.
arr_2d = np.random.randint(1, 25, [5, 5])
print(arr_2d)

# Sử dụng cắt lát để lấy một phần mảng từ hàng thứ 2 đến hàng thứ 4 và từ cột thứ 1 đến cột thứ 3
print(f"mảng từ hàng thứ 2 đến hàng thứ 4 và từ cột thứ 1 đến cột thứ 3 là :\n{arr_2d[1:4, 0:3]}")

# Tính và in ra giá trị trung bình của từng hàng và từng cột trong phần mảng vừa cắt
print("Giá trị trung bình của từng hàng:", np.mean(arr_2d, axis=1))
print("Giá trị trung bình của từng cột:", np.mean(arr_2d, axis=0))

# Tìm và in ra giá trị lớn nhất và nhỏ nhất trong phần mảng vừa cắt
print("Giá trị lớn nhất trong phần mảng:", np.max(arr_2d))
print("Giá trị nhỏ nhất trong phần mảng:", np.min(arr_2d))

# Đảo ngược thứ tự của từng hàng trong phần mảng và in ra phần mảng sau khi đã đảo ngược
print("Phần mảng sau khi đảo ngược hàng:\n", arr_2d[::,::-1])