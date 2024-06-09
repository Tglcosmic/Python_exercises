#sử dụng kiểu list, hàm for với mỗi phần tử được nhập cách nhau bởi dấu phẩy để nhập dãy số
day_so = [int(x) for x in input("Nhập dãy số bất kì cách nhau bởi dấu phẩy: ").split(",")]

#sắp xếp dãy số theo chiều tăng dần và in nó ra
day_so.sort()
min_day_so = day_so[0]
print(day_so)
print("phần tử có giá trị nhỏ nhất là: ", min_day_so)

#tạo biến tổng số chia hết cho 3 và bộ đếm với giá trị ban đầu bằng 0 (a: tổng, b: bộ đếm)
a = 0
b = 0

#dùng vòng lặp for với điều kiện chỉ số chia hết cho 3. cộng các phần tử lại cùng lúc đó chạy bộ đếm
for n in day_so:
    if n % 3 == 0:
        a += n
        b += 1

#dùng if để tìm số lớn hơn 3 và tính trung bình cộng
if a > 3:
    tb = a/b
    print("trung bình cộng các phân tử chia hết cho 3 là: ", tb)
else:
    print("không có phần tử nào chia hết cho 3")