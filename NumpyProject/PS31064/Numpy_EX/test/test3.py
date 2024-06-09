import numpy as np

# arr_a = np.array([2, 4, 6])
# ls_index = [1, 2]
# print(np.insert(arr_a, ls_index, 99))


# print(arr_a * arr_b)    # phép nhân
# print(np.dot(arr_a, arr_b))     # phép tích

# print(np.append(arr_a, [11, 22, 33]))

arr_b = np.array([[2, 4, 6],[3, 5, 7]])
ls = [11, 22, 33]
print(arr_b)
print(np.insert(arr_b, 1, ls, axis=1))