import numpy as np
from datetime import datetime, timedelta

# Tạo một mảng NumPy chứa 15 ngày tháng ngẫu nhiên trong khoảng thời gian năm nay
start_date = datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
end_date = datetime.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
num_days = 15
random_dates = np.array([start_date + timedelta(days=np.random.randint((end_date - start_date).days)) for _ in range(num_days)])

# 1. Tìm và in ra ngày gần nhất và xa nhất trong mảng
nearest_date = min(random_dates, key=lambda x: abs(datetime.now() - x))
farthest_date = max(random_dates, key=lambda x: abs(datetime.now() - x))
print("Ngày gần nhất trong mảng:", nearest_date)
print("Ngày xa nhất trong mảng:", farthest_date)

# 2. Tính và in ra số ngày chênh lệch giữa các cặp ngày liên tiếp trong mảng
differences = np.diff(random_dates).astype('timedelta64[D]').astype(int)
print("Số ngày chênh lệch giữa các cặp ngày liên tiếp trong mảng:", differences)

# 3. Sắp xếp mảng theo thứ tự tăng dần và in ra kết quả
sorted_dates = np.sort(random_dates)
sorted_dates_str = [date.strftime("%Y-%m-%d") for date in sorted_dates]
print("Mảng sau khi được sắp xếp theo thứ tự tăng dần:", sorted_dates_str)

# 4. Tạo một mảng chứa các ngày trong tuần của mảng ban đầu và in ra kết quả
weekdays = np.array([date.strftime("%A") for date in random_dates])
print("Các ngày trong tuần của mảng ban đầu:", weekdays)

# 5. In ra số lần xuất hiện của từng thứ trong mảng
unique_weekdays, counts = np.unique(weekdays, return_counts=True)
print("Số lần xuất hiện của từng thứ trong mảng:")
for weekday, count in zip(unique_weekdays, counts):
    print(f"{weekday}: {count} lần")
