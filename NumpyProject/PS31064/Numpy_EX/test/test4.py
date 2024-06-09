import numpy as np
# path_file = r"H:\Python exercises\NumpyProject\PS31064\Numpy_EX\test\demo.txt"
# data_raw = np.loadtxt(path_file, delimiter=",",dtype="int")
# data_new = np.delete(data_raw, 0, axis=0)
# data_new_2 = np.delete(data_raw,[1,3,5], axis=1)
# np.savetxt("demo_ghifile.txt", data_new_2, delimiter=",", fmt="%d")

# path_file = r"covid_19_data_Copy.csv"
# data_raw = np.genfromtxt(path_file, delimiter=",", usecols=[5,6,7], skip_header=0, dtype=int)
# print(np.shape(data_raw))
# print(np.sort(data_raw[:,0])[::-1])
# arr_a = np.array([2,4,6,3,5,8,4])
# print(np.sort(arr_a))
# print(arr_a)

# ls_monhoc= ["toan", "ly", "hoa"]
# arr_monhoc = np.array(ls_monhoc)
#
# def add_monhoc(monhoc):
#     global arr_monhoc
#     arr_monhoc = np.append(arr_monhoc, monhoc)
#     print(arr_monhoc)
# add_monhoc("su")

import numpy as np
a = "demo_ghifile.csv"
SNo,ObservationDate,Province_State,Country_Region,Last_Update,Confirmed,Deaths,Recovered = np.genfromtxt(a
,delimiter=",", usecols=[0,1,2,3,4,5,6,7], skip_header=1, dtype=None, unpack=True)

columns_to_keep = ['ObservationDate', 'Province_State', 'Country_Region', 'Confirmed', 'Deaths', 'Recovered']
df_cleaned = np.array([ObservationDate,Country_Region,Confirmed,Deaths,Recovered])


date = ObservationDate
Confirmed_case = Confirmed
deaths = Deaths

# max_Confirmed_idx = np.argmax(Confirmed_case)
# max_Confirmed_date = date[max_Confirmed_idx]
# print(max_Confirmed_date)
df_sorted_by_date = np.sort(df_cleaned)[::,::1]
print(df_cleaned)
print("------------------------")
print(df_sorted_by_date)