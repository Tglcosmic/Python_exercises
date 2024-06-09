import numpy as np
rd_1d = np.random.randint(1, 10, size=10)
rd_2d = np.random.randint(1, 10, size=(2, 5))

print("mảng 1 chiều ngẫu nhiên từ 1 đến 10:")
print(rd_1d)

print("\nmảng 1 chiều ngẫu nhiên từ 1 đến 10 theo chiều tăng dần:")
sorted_1d_up = np.sort(rd_1d)
print(sorted_1d_up)

print("\nmảng 1 chiều ngẫu nhiên từ 1 đến 10 theo chiều giảm dần:")
sorted_1d_down = np.sort(rd_1d)[::-1]
print(sorted_1d_down)

print("\nmảng 2 chiều ngẫu nhiên từ 1 đến 10: ")
print(rd_2d)

print("\nmảng 2 chiều ngẫu nhiên từ 1 đến 10 theo chiều tăng dần theo hàng:")
sorted_2d_r_up = np.sort(rd_2d) # Sắp xếp hàng theo kiểu tăng dần
print(sorted_2d_r_up)

print("\nmảng 2 chiều ngẫu nhiên từ 1 đến 10 theo chiều tăng dần theo cột:")
sorted_2d_c_up = np.sort(rd_2d, axis=0) # Sắp xếp cột theo kiểu tăng dần
print(sorted_2d_c_up)

print("\nmảng 2 chiều ngẫu nhiên từ 1 đến 10 theo chiều giảm dần theo hàng:")
sorted_2d_r_down = np.sort(rd_2d)[:, ::-1] # Sắp xếp hàng theo chiều giảm dần
print(sorted_2d_r_down)

print("\nmảng 2 chiều ngẫu nhiên từ 1 đến 10 theo chiều giảm dần theo cột:")
sorted_2d_c_down = np.sort(rd_2d, axis=0)[::-1] # Sắp xếp cột theo chiều giảm dần
print(sorted_2d_c_down)