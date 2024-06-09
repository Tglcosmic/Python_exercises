import numpy as np      # import thư viện Numpy

list1 = np.array([3, 7, 10, 12, 5])         # Tạo một mảng chứa các số nguyên bất kì

# Sử dụng hàm MEAN để trung bình cộng các phần tử và xuất ra màn hình
print('Trung bình cộng của list:', np.mean(list1))

vector = np.array([1, 2, 3, 4, 5, 6])       #Tạo Vector

# Sử dụng hàm SUM để tính tổng các phần tử trong vector và in ra màn hình
print('Tổng các phần tử trong một vector là:', np.sum(vector))
matrix = np.array([[1, 2, 3],       #Tạo một ma trận
                   [1, 2, 3],
                   [1, 2, 3]])
#Sử dụng hàm SUM và lần này ta xét tổng phần tử theo cột, Np.sum.("Đối tượng", axis="chiều(0: dọc, 1: ngang)")
print('Tổng các phần tử trong 1 ma trận theo cột là:', np.sum(matrix, axis=0))
