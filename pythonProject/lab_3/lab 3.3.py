#nhập số nguyên tố từ bàn phím
n = int(input("Nhập số một số nguyên: "))

#tạo biến kiểm tra và đặt i = 2
ok = True
i = 2

#Tạo cú pháp kiểm tra bằng lệnh while điều kiện nếu chia hết cho i vòng lặp sẽ dừng
#(giá trị sẽ tăng cho đến khi số đó thực sự không chia hết cho i)
while i < n:
    if n % i == 0:
        ok = False
        break
    i += 1

#dùng if nếu ok là True và n > 1 thì số đó là số nguyên tố
if ok and n > 1:
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không là số nguyên tố")