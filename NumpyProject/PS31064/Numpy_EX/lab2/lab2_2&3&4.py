import numpy as np

m = np.array([[1, 2, 3],
              [4, 5, 6]])

sum_m = np.sum(m)
min_m = np.min(m)
max_m = np.max(m)
mean_m = np.mean(m)

# print(f'Tổng của phần tử là {sum_m}, lớn nhất là {max_m} và nhỏ nhất là {min_m}, trung bình là {mean_m}')


# Tạo một mảng từ một list lồng nhau chứa các giá trị số nguyên
list = [[1, 2, 1], [3, 5, 7], [2, 4, 9]]
list_a = np.array(list)
print("Mảng từ list lồng nhau chứa số nguyên:")
print(list_a)

# Tạo một mảng từ một tuple lồng nhau chứa các giá trị số thực
tuple = ((3.2, 2.1, 6.3), (4.1, 2.5, 6.4), (2.7, 1.8, 9.3))
tuple_a = np.array(tuple)
print("\nMảng từ tuple lồng nhau chứa số thực:")
print(tuple_a)

# Dictionary
print("\nMảng từ dictionary chứa các list có chiều dài khác nhau:")
dict_ls = {'a': [1, 9, 6], 'b': [5, 6], 'c': [2, 6, 4, 6]}
value = []
for v in dict_ls:
    value.append(dict_ls[v])
print(value)

# Tạo một mảng 2x3 chứa các giá trị ngẫu nhiên từ phân phối chuẩn
rd_ar = np.random.randn(2, 3)
print("Mảng 2x3 chứa các giá trị ngẫu nhiên từ phân phối chuẩn:")
print(rd_ar)

# Tạo một dãy số từ 0 đến 100 với bước nhảy là 10
seq_ar = np.arange(0, 10)
print("\nDãy số từ 0 đến 100 với bước nhảy là 10:")
print(seq_ar)

# Tạo một mảng 5 phần tử chứa các giá trị cách đều từ 1 đến 10
ev_s_ar = np.linspace(1, 10, 5)
print("\nMảng 5 phần tử chứa các giá trị cách đều từ 1 đến 10:")
print(ev_s_ar)

# Tạo một mảng 3x4 chứa các giá trị zeros
zeros_ar = np.zeros((3, 4))
print("\nMảng 3x4 chứa các giá trị zeros:")
print(zeros_ar)
