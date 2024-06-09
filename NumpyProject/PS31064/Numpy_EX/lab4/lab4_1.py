import numpy as np

# Mảng NumPy
arr = np.array([[1.234, 2.345, 3.456],
                [4.567, 5.678, 6.789],
                [7.890, 8.901, 9.012]])


# 1.Sắp xếp theo dòng, định dạng cột theo chuẩn, delimiter tab
np.savetxt('lab4_1.txt', arr, fmt='%.18e', delimiter='\t')

# 1.Sắp xếp theo cột, định dạng cột làm tròn đến 2 chữ số thập phân, delimiter phẩy
np.savetxt('lab4_2.txt', np.round(arr, 2), fmt='%.2f', delimiter=',')

# 1.Sắp xếp theo cột, định dạng cột là số nguyên, delimiter khoảng trắng
np.savetxt('lab4_3.txt', arr.astype(int), fmt='%d', delimiter=' ')

# 1.Sắp xếp theo dòng, định dạng cột làm tròn đến 3 chữ số thập phân, delimiter @
np.savetxt('lab4_4.txt', np.round(arr, 3), fmt='%.3f', delimiter='@')


# 2.Đọc file và in nội dung
files = ['lab4_1.txt', 'lab4_2.txt', 'lab4_3.txt', 'lab4_4.txt']
for file in files:
    with open(file, 'r') as f:
        content = np.loadtxt(file, delimiter='\t' if 'lab4_1' in file else ',' if 'lab4_2' in file else ' ' if 'lab4_3' in file else '@')
    print(f"Nội dung của {file}:")
    print(content)

