import numpy as np

# Tạo một mảng NumPy có 10 phần tử số nguyên ngẫu nhiên từ -50 đến 50
random_array = np.random.randint(-50, 51, 10)

# 1. Tìm và in ra giá trị lớn nhất và nhỏ nhất trong mảng
max_value = np.max(random_array)
min_value = np.min(random_array)
print("Giá trị lớn nhất trong mảng là:", max_value)
print("Giá trị nhỏ nhất trong mảng là:", min_value)

# 2. Tính và in ra tổng các phần tử dương trong mảng
positive_sum = np.sum(random_array[random_array > 0])
print("Tổng các phần tử dương trong mảng là:", positive_sum)

# 3. Tính và in ra độ lệch chuẩn của mảng
std_deviation = np.std(random_array)
print("Độ lệch chuẩn của mảng là:", std_deviation)

# 4. Sắp xếp mảng theo thứ tự giảm dần và in ra kết quả
sorted_array = np.sort(random_array)[::-1]
print("Mảng sau khi được sắp xếp theo thứ tự giảm dần:", sorted_array)

# 5. In ra mảng sau khi loại bỏ các phần tử trùng lặp
unique_array = np.unique(random_array)
print("Mảng sau khi loại bỏ các phần tử trùng lặp:", unique_array)
