# Xuất các bảng cửu chương theo dãy ngang
#vòng lặp lồng vòng lặp sẽ chạy hết j từ 1 đến 10 trong từng giá trị của i tạo thành từng bảng cửu chương
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}",end="\t") # hàm end="\t" sẽ thay đổi xuống dòng thành tab
    print()  # Xuống dòng sau khi hoàn thành một bảng cửu chương
