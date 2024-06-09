import numpy as np

arr = np.array([[1.234, 2.345, 3.456],
                [4.567, 5.678, 6.789],
                [7.890, 8.901, 9.012]])
array = np.sort(arr.transpose())[::-1]
print(array)
load = np.savetxt("lab4+.txt",array ,delimiter=';')
show = np.loadtxt("lab4+.txt", delimiter=';', dtype=float)
arr_dau = show[:, 0]
arr_cuoi = show[:, -1]

print(arr_dau)
print(arr_cuoi)