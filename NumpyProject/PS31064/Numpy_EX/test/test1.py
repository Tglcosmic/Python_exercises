import numpy as np
# ls1 = [2, 4, 6, 3, 5, 7]
# print(ls1)

# np1 = np.array([[3, 5, 7],[2, 4, 6]])
# print(np1)
# print(np1[0, 1])
# print(np1[1, 1])

ls2 = np.array([3, 7, 10, 12, 5])
print(np.average(ls2))
print(np.sum(ls2))

matrix = np.array([[3, 5, 7], [2, 4, 6], [7, 8, 9]])
print(matrix)
print('Tổng các phần tử trong ma trận theo cột là: ', np.sum(matrix, axis=0))