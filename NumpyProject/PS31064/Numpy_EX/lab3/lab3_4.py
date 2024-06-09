import numpy as np

# 1. Tìm Kiếm Trong Mảng 1 Chiều
print("1. Tìm Kiếm Trong Mảng 1 Chiều:")
# Tạo một mảng 1 chiều ngẫu nhiên
arr_1d = np.random.randint(0, 100, 10)
print("Mảng 1 chiều:", arr_1d)

# Tìm vị trí của các phần tử có giá trị lớn hơn một ngưỡng nhất định
threshold = 50
indices_above_threshold = np.where(arr_1d > threshold)[0]
print(f"Các phần tử lớn hơn {threshold} có vị trí là:", indices_above_threshold)

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất trong mảng
index_of_max = np.argmax(arr_1d)
index_of_min = np.argmin(arr_1d)
print(f"Vị trí của phần tử lớn nhất ({arr_1d[index_of_max]}) là: {index_of_max}")
print(f"Vị trí của phần tử nhỏ nhất ({arr_1d[index_of_min]}) là: {index_of_min}")

# 2. Tìm Kiếm Trong Mảng 2 Chiều
print("\n2. Tìm Kiếm Trong Mảng 2 Chiều:")
# Tạo một mảng 2 chiều với các giá trị ngẫu nhiên
arr_2d = np.random.randint(0, 100, (5, 5))
print("Mảng 2 chiều:\n", arr_2d)

# Tìm vị trí của các phần tử có giá trị lớn hơn một ngưỡng nhất định
nguong_2chieu = 70
so_tren_nguong_2chieu = np.where(arr_2d > nguong_2chieu)
print(f"Các phần tử lớn hơn {nguong_2chieu} có vị trí là:")
for i in range(len(so_tren_nguong_2chieu[0])):
    print(f"({so_tren_nguong_2chieu[0][i]}, {so_tren_nguong_2chieu[1][i]})")

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất trong mảng 2 chiều
index_of_max_2d = np.unravel_index(np.argmax(arr_2d), arr_2d.shape)
index_of_min_2d = np.unravel_index(np.argmin(arr_2d), arr_2d.shape)
print(f"Vị trí của phần tử lớn nhất ({arr_2d[index_of_max_2d]}) là: {index_of_max_2d}")
print(f"Vị trí của phần tử nhỏ nhất ({arr_2d[index_of_min_2d]}) là: {index_of_min_2d}")

print('\n-- 2 cách khác --\n')

position_max = np.argmax(arr_2d)
position_min = np.argmin(arr_2d)

number_d = arr_2d.shape

row1 = position_max / number_d[1]
column1 = position_max % number_d[1]

row2 = position_min / number_d[1]
column2 = position_min % number_d[1]

p_max = np.divmod(position_max, number_d[1])
p_min = np.divmod(position_min, number_d[1])

print(f"Vị trí của phần tử lớn nhất ({arr_2d[p_max]}) là: ({int(row1)}, {column1})")
print(f"Vị trí của phần tử nhỏ nhất ({arr_2d[p_min]}) là: ({int(row2)}, {column2})")

print(f"Vị trí của phần tử lớn nhất ({arr_2d[p_max]}) là: {p_max})")
print(f"Vị trí của phần tử nhỏ nhất ({arr_2d[p_min]}) là: {p_min})")