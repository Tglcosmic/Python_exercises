import numpy as np

filepath = r"covid_19_data_Copy.csv"

# Y1.01 Tạo một mảng NumPy chứa số liệu
data_raw_y11 = np.genfromtxt(filepath,delimiter=",", usecols=[5,6,7], skip_header=1, dtype=int)
canhiem = np.array(data_raw_y11[:, 0])
cachet = np.array(data_raw_y11[:, 1])
cahoiphuc = np.array(data_raw_y11[:, 2])
print(canhiem)
print(cachet)
print(cahoiphuc)






