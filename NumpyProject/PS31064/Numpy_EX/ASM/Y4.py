import numpy as np

filepath = r"covid_19_data_Copy.csv"

# Y1.04
# Xác định ngày có số ca nhiễm và tử vong cao nhất và thấp nhất.
ObservationDate,Confirmed,Deaths,Recovered = np.genfromtxt(filepath,
delimiter=",", usecols=[1,5,6,7], skip_header=1, dtype=None, encoding="UTF-8", unpack=True)

max_Confirmed_idx = np.argmax(Confirmed)
max_Confirmed_date = ObservationDate[max_Confirmed_idx]
min_Confirmed_idx = np.argmin(Confirmed)
min_Confirmed_date = ObservationDate[max_Confirmed_idx]
print(f'Ngày có số ca nhiểm cao nhất là {max_Confirmed_date} với {Confirmed[max_Confirmed_idx]} ca nhiễm')
print(f'Ngày có số ca nhiểm thấp nhất là {min_Confirmed_date} với {Confirmed[min_Confirmed_idx]} ca nhiễm')
max_Deaths_idx = np.argmax(Deaths)
max_Deaths_date = ObservationDate[max_Deaths_idx]
min_Deaths_idx = np.argmin(Deaths)
min_Deaths_date = ObservationDate[min_Deaths_idx]
print(f'Ngày có số ca chết cao nhất là {max_Deaths_date} với {Deaths[max_Deaths_idx]} ca chết')
print(f'Ngày có số ca chết thấp nhất là {min_Deaths_date} với {Deaths[min_Deaths_idx]} ca chết')

# Tìm ngày có số ca nhiễm tăng mạnh nhất so với ngày trước đó.
daily_increase = np.diff(Confirmed)
max_increase_idx = np.argmax(daily_increase)
max_increase_date = ObservationDate[max_increase_idx + 1]
print(f"Ngày có ca nhiễm tăng mạnh nhất là {max_increase_date}")

# Xác định ngày có số ca hồi phục nhiều nhất.
max_Recovered_idx = np.argmax(Recovered)
max_Recovered_date = ObservationDate[max_Recovered_idx]
print(f"Ngày có số ca hồi phục nhiều nhất là {max_Recovered_date}")