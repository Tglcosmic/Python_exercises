import numpy as np
# Tạo một mảng NumPy 2 chiều kích thước 3x4 với dữ liệu là số nguyên từ 1 đến 12.
arr_2d = np.arange(1, 13).reshape(3,4)
print(arr_2d)
print(f"hình dạng của mảng là: {np.shape(arr_2d)}")
tp_dm = np.transpose(arr_2d)
print(f"Chuyển vị:\n {tp_dm}")
print(f"Hình dạng của mảng sau khi chuyển vị: {np.shape(tp_dm)}")
new_arr = tp_dm.reshape(2, 3, 2)
print(f"Mảng mới có có hình dạng 2 chiều với kích thước 3*2:\n {new_arr}")
print(f"Kích thước mảng mới là: {np.shape(new_arr)}")