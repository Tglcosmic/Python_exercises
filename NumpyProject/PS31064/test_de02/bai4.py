import numpy as np

t = np.linspace(18, 38.5, 42)
temp = t.reshape(6, 7)
print(temp)

# Lấy dữ liệu của tỉnh có nhiệt độ trung bình cao nhất trong 7 ngày
print(f"Tỉnh có nhiệt độ trung bình cao nhất trong 7 ngày là tỉnh số {np.argmax(np.mean(temp, axis=1)) + 1}")

# Lấy dữ liệu 2 ngày cuối tuần của tỉnh thứ 5 trong mảng
day2_5 = temp[4, -2:]
print(f"Dữ liệu 2 ngày cuối tuần của tỉnh thứ 5: {day2_5}")

# Tính khoảng cách chênh lệch nhiệt độ của 2 ngày liền kề của từng tỉnh
temp_diff = np.diff(temp, axis=0)
print("Khoảng cách chênh lệch nhiệt độ của 2 ngày liền kề của từng tỉnh:")
print(temp_diff)
