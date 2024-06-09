import numpy as np

filepath = r"covid_19_data_Copy.csv"
# Y1.05
# Tách dữ liệu của một quốc gia cụ thể để tập trung phân tích sâu hơn. In mảng các quốc gia không trùng lặp
unique_country = np.loadtxt(filepath, delimiter=',', skiprows=1, dtype=str, encoding='UTF-8')
print(f"Danh sách các quốc gia: {np.unique(unique_country)}")

data_raw_y15 = np.genfromtxt(filepath, delimiter=',',names=True , dtype=None, encoding='UTF-8')
# Lọc dữ liệu để chỉ lấy thông tin của một quốc gia xác định.
target_country = 'Vietnam'
data_raw_y15_VN = data_raw_y15[data_raw_y15["CountryRegion"] == target_country]
print(data_raw_y15_VN)