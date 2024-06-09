import numpy as np

filepath = r"H:\Python exercises\NumpyProject\PS31064\Numpy_EX\test\covid_19_data_Copy.csv"

# Y1.02 Loại bỏ các cột không cần thiết từ mảng.
data_raw_y12 = np.genfromtxt(filepath, delimiter=",", dtype=str, encoding="UTF-8")
cleaned_data = np.delete(data_raw_y12, (0, 2, 4), axis=1)
print(cleaned_data)