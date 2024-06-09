import numpy as np

# arr = np.array([2, 4, 6], dtype=np.str_)
# print(arr)


dtype = np.dtype([("name", np.str_, 20), ("age", np.int_)])
sinhvien = np.array([("tommy shelby", 20),("thomas shelby", 30)], dtype=dtype)
print(sinhvien)


dict_ls = {'a': [1, 9, 6], 'b': [5, 6], 'c': [2, 6, 4, 6]}
# Duyệt qua từng cặp key-value trong từ điển
for key, value in dict_ls.items():
    # Tạo mảng từ danh sách giá trị
    arr = np.array(value)
    # In tên của mảng
    print(f"Array from dictionary key '{key}':", arr)