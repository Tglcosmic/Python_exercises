# khai báo thư viện
import math

#input
a = float(input("nhập dự liệu vào a: "))
b = float(input("nhập dự liệu vào b: "))
c = float(input("nhập dự liệu vào c: "))

#xử lí
if a==0:
    x = -c/b
    print("Phương trình bậc 1 có kết quả là: %0.2f" %x)
elif a!=0:
    d = b ** 2 - a * c
    if d < 0:
        print("Phương trình vô nghiệm")
    elif d == 0:
        X: float = -b/(2*a)
        print(f'Phương trình có nghiệm kép: {X}',(X))
    else:
        X1 = (-b+math.sqrt(d)/(2*a))
        x1 = round(X1,2)
        X2 = (-b-math.sqrt(d)/(2*a))
        x2 = round(X2,2)
        print(f'Phương trình có 2 nghiệm phân biệt: {x1}, {x2}')