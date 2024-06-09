import numpy as np

# Tạo một mảng NumPy một chiều có 10 phần tử với dữ liệu ngẫu nhiên từ 1 đến 100
arr_1d = np.random.randint(1, 100, 10)
print(arr_1d)

# Sử dụng chỉ mục để lấy giá trị của phần tử cuối cùng trong mảng
print(f"giá trị cuối cùng trong mảng: {arr_1d[-1]}")

# Tìm và in ra giá trị lớn nhất và nhỏ nhất trong mảng
print(f"Giá trị lớn nhất là {np.max(arr_1d)} và nhỏ nhất là {np.min(arr_1d)}")

# Tính và in ra độ lệch chuẩn của mảng
std_deviation = np.std(arr_1d)
print("Độ lệch chuẩn của mảng:", std_deviation)

# Đảo ngược thứ tự các phần tử trong mảng và in ra mảng sau khi đã đảo ngược
reversed_arr = arr_1d[::-1]
print("Mảng sau khi đảo ngược:", reversed_arr)