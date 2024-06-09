#input
a = float(input("nhập dự liệu vào a: "))
b = float(input("nhập dự liệu vào b: "))

#xử lí và output (sử dụng lồng hàm if để kiểm tra a rồi đến b)
if a==0:
    if b==0:
        print("thông báo vô số nghiệm")
    else:
        print("thông báo vô nghiệm")
else:
    print('kết quả phương trình bậc 1 là: ',(-b/a))
