import numpy as np

filepath = r"covid_19_data_Copy.csv"
#Y1.06
# Tính tổng số ca nhiễm, tử vong và hồi phục để hiểu quy mô của dịch bệnh.
data_raw_y16 = np.genfromtxt(filepath, delimiter=',', dtype=None, names=True, encoding='UTF-8')
print(f"Tổng số ca nhiễm: {np.sum(data_raw_y16['Confirmed'])}")
print(f"Tổng số ca tử vong: {np.sum(data_raw_y16['Deaths'])}")
print(f"Tổng số ca hồi phục: {np.sum(data_raw_y16['Recovered'])}")

# Tính tổng số ca nhiễm từ một số quốc gia được chọn.
lscountries = ['Vietnam','France']
sum_confirmed = np.sum([np.sum(data_raw_y16[data_raw_y16['CountryRegion'] == country]['Confirmed']) for country in lscountries])
print(f'Tổng số ca nhiễm theo quốc gia được chọn bao gồm {lscountries} là {sum_confirmed}')

# Tính tổng số ca tử vong từ ngày đầu tiên cho đến ngày hiện tại.
print(f"Tổng số ca tử vong từ ngày đầ tiền đến hiện tại: {np.sum(data_raw_y16['Deaths'])}")