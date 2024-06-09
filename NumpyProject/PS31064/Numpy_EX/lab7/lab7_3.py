import numpy as np

# Tạo ma trận 3x3 với dữ liệu số nguyên từ 1 đến 9
matrix = np.arange(1, 10).reshape(3, 3)
print("Ma trận ban đầu:\n", matrix)

# 1. Tính định thức của ma trận và in ra kết quả
determinant = np.linalg.det(matrix)
print("Định thức của ma trận là:", determinant)

# 2. Tìm ma trận nghịch đảo của ma trận ban đầu và in ra ma trận nghịch đảo
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Ma trận nghịch đảo của ma trận ban đầu là:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Ma trận ban đầu không khả nghịch.")

# 3. Tính và in ra ma trận chuyển vị của ma trận ban đầu
transpose_matrix = np.transpose(matrix)
print("Ma trận chuyển vị của ma trận ban đầu là:")
print(transpose_matrix)

# 4. Tính và in ra tích của ma trận với chính nó
product_matrix = np.dot(matrix, matrix)
print("Tích của ma trận với chính nó là:")
print(product_matrix)

# 5. In ra ma trận với các phần tử âm được thay thế bằng 0
matrix_nonnegative = np.where(matrix < 0, 0, matrix)
print("Ma trận với các phần tử âm được thay thế bằng 0:")
print(matrix_nonnegative)
