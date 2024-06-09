import numpy as np
import Y2
import Y5
# Lưu trữ dữ liệu của một quốc gia cụ thể sau khi đã xử lý vào một file.

np.savetxt("cleaned_data.txt", Y2.cleaned_data, delimiter=",", fmt='%s')
np.savetxt("VN_data.csv", Y5.data_raw_y15_VN, delimiter=",", fmt='%s', )
np.savetxt("cleaned_data.csv", Y2.cleaned_data, delimiter=",", fmt='%s')