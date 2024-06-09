import numpy as np

arr_Int = np.random.randint(-5, 50, 200)
# print(arr_Int)

# Chuyển đổi arr_Int thành mảng 2 chiều có 5 cột và số dòng tự động.
arr_Int_2D = arr_Int.reshape(-1, 5)
print(arr_Int_2D)

# Thực hiện nhân mảng với 0.8 và chuyển đổi kiểu dữ liệu của mảng sang float32 bằng astype()
cal = (arr_Int_2D * 0.8).astype(dtype='float32')
print(cal)

# Lọc bỏ các giá trị âm
arr_cleaned = cal[cal >= 0]

# Sắp xếp mảng
arr_cleaned_sort = np.sort(arr_cleaned)

# Ghi ra file
np.savetxt('output.txt', arr_cleaned_sort, fmt='%.3f', delimiter='@')
