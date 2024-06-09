import numpy as np

daily_t = np.array([25.6, 26.3, 24.8, 27.5, 23.9, 25.1, 26.7])

temp_a = daily_t.astype(np.float32)
print(temp_a)

ave_temp = np.average(temp_a)
print(f'Nhiệt độ trung bình hằng ngày là: {ave_temp}')

max_temp = np.max(daily_t)
min_temp = np.min(daily_t)
print(f'Nhiệt độ cao nhất là {max_temp} và thấp nhất là {min_temp}')