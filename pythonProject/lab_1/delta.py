#thư viện math
import math

#tính delta
a = float(input("Nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))

d = b * b - 4 * a * c
print('Kết quả căn bậc 2 của delta là:', math.sqrt(abs(d)))