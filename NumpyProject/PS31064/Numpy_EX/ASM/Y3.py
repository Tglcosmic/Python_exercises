import numpy as np

filepath = r"covid_19_data_Copy.csv"
# Y1.03 Sắp xếp các theo cột
data_raw_y13 = np.genfromtxt(filepath, delimiter=",", dtype=None, names=True, encoding="UTF-8")
print(data_raw_y13)
# Sắp xếp mảng theo thời gian khảo sát để hiểu rõ hơn về xu hướng phát triển của dịch bệnh.
print(np.sort(data_raw_y13, order='ObservationDate'))
# Sắp xếp dữ liệu theo số ca nhiễm từ thấp đến cao để xác định các quốc gia ổn định.
print(np.sort(data_raw_y13, order='Confirmed'))
# Sắp xếp mảng theo thứ tự tử vong tăng dần để đánh giá tình hình nguy cấp.
print(np.sort(data_raw_y13, order='Deaths'))
