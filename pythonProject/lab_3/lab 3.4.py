#vòng lặp lồng vòng lặp sẽ chạy hết j từ 1 đến 10 trong từng giá trị của i tạo thành từng bảng cửu chương
for i in range(1, 10):
    print(f"Bảng cửu chương {i}: ")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print()  # Xuống dòng sau khi hoàn thành một bảng cửu chương
