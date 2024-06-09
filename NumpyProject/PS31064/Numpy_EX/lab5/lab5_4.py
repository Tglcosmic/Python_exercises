import numpy as np

#1. Tạo một mảng NumPy một chiều với dữ liệu số nguyên từ -10 đến 10.
arr_1d = np.arange(-10, 11)
# print(arr_1d)
# #2. Sử dụng điều kiện để truy cập các phần tử trong mảng có giá trị dương
# arr_duong = arr_1d[arr_1d > 0]
# print("\nCác phần tử dương trong mảng:", arr_duong)
# #3. Tính và in ra tổng, trung bình và số lượng các phần tử thỏa điều kiện trên.
# print("Tổng các phần tử dương trong mảng:", np.sum(arr_duong))
# print("Trung bình các phần tử dương trong mảng:", np.mean(arr_duong))
# print("Số lượng các phần tử dương trong mảng:", len(arr_duong))
# #4. Tìm và in ra các phần tử là số nguyên tố trong mảng.
prime_elements = [x for x in arr_1d if all(x % i for i in range(2, x)) and x > 1]
print("\nCác phần tử là số nguyên tố trong mảng:", prime_elements)
# #5. In ra mảng sau khi loại bỏ các phần tử trùng lặp.
# trunglap_arr = np.unique(arr_1d)
# print("\nMảng sau khi loại bỏ các phần tử trùng lặp:", trunglap_arr)