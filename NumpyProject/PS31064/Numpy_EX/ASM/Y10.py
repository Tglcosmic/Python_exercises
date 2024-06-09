import numpy as np

filepath = r"covid_19_data_Copy.csv"

# Đọc dữ liệu từ file CSV
data = np.loadtxt(filepath, delimiter=',', skiprows=1, dtype=str)
daily_cases = data[:, 5]
daily_deaths = data[:, 6]
daily_recoveries = data[:, 7]

# Tính trung bình số ca nhiễm, tử vong, và hồi phục mỗi ngày để hiểu xu hướng trung bình.
print(np.mean(daily_cases))