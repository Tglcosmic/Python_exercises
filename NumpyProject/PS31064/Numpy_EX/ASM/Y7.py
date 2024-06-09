import numpy as np

filepath = r"covid_19_data_Copy.csv"
# Y1.07
ObservationDate,Confirmed,Deaths,Recovered = np.genfromtxt(filepath,
delimiter=",", usecols=[1,5,6,7], skip_header=1, dtype=None, encoding="UTF-8", unpack=True)

max_Confirmed_idx = np.argmax(Confirmed)
max_Confirmed_date = ObservationDate[max_Confirmed_idx]
print(f'Ngày có số ca nhiểm cao nhất là {max_Confirmed_date} với {Confirmed[max_Confirmed_idx]} ca nhiễm')
max_Deaths_idx = np.argmax(Deaths)
max_Deaths_date = ObservationDate[max_Deaths_idx]
print(f'Ngày có số ca chết cao nhất là {max_Deaths_date} với {Deaths[max_Deaths_idx]} ca chết')

# Tìm ngày có số ca nhiễm tăng mạnh sau chuỗi ngày ổn định
stable_days = 5  # Định nghĩa số ngày ổn định
threshold_increase = 50  # Định nghĩa ngưỡng tăng mạnh
for i in range(len(Confirmed) - stable_days):
    if all(Confirmed[i + j] - Confirmed[i + j - 1] > threshold_increase for j in range(1, stable_days + 1)):
        next_day = i + stable_days
        print(f'Ngày có số ca nhiễm tăng mạnh sau chuỗi ngày ổn định là {ObservationDate[next_day]} với {Confirmed[next_day]} ca nhiễm')
        break
else:
    print("Không có ngày nào có số ca nhiễm tăng mạnh sau chuỗi ngày ổn định.")
# Xác định ngày có số ca hồi phục đột ngột
for i in range(1, len(Recovered)):
    if Recovered[i] - Recovered[i - 1] > 500:  # Định nghĩa ngưỡng đột ngột
        print(f'Ngày có số ca hồi phục đột ngột là {ObservationDate[i]} với {Recovered[i]} ca hồi phục')
        break
else:
    print("Không có ngày nào có số ca hồi phục đột ngột.")