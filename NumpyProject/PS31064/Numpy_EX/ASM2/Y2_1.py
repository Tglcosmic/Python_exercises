import numpy as np

filepath = r"covid_19_data_Copy.csv"
data_raw = np.genfromtxt(filepath,delimiter=",", usecols=[1,3,5,6,7], skip_header=1, dtype=str, encoding="UTF-8")
# Lấy một phần dữ liệu từ mảng số ca nhiễm để phân tích xu hướng
unique_dates = np.unique(data_raw[:, 0])
date_10days = np.sort(unique_dates)[0:10]
data_raw_10days = [data_raw[data_raw[:, 0] == x] for x in date_10days]
print(data_raw_10days)

# Create a boolean index array using np.isin()
boolean_index = np.isin(data_raw[:, 0], date_10days)

# Use the boolean index array to filter the data
Data_raw_10days = data_raw[boolean_index]
# Lựa chọn các quốc gia
quocgia = ['Vietnam', 'Malaysia', 'Philippines']

# Lấy dữ liệu số ca nhiễm và số ca hồi phục
data_quocgia = data_raw[np.isin(data_raw[:, 1], quocgia)]

# Tính tỷ lệ hồi phục
tilehoiphuc = {}
for country in quocgia:
    so_ca_nhiem = np.sum(data_quocgia[data_quocgia[:, 1] == country][:, 2].astype(int))
    so_ca_hoi_phuc = np.sum(data_quocgia[data_quocgia[:, 1] == country][:, 4].astype(int))
    if so_ca_nhiem > 0:
        tilehoiphuc[country] = so_ca_hoi_phuc / so_ca_nhiem
    else:
        tilehoiphuc[country] = 0
# In kết quả
for country, tile in tilehoiphuc.items():
    print(f"Tỷ lệ hồi phục {country}: {tile:.2%}")