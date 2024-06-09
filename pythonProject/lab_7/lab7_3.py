import csv
try:
    with open("lab_7_3.csv", "x", encoding="utf"):
        for i in range(3):
            tieu_de = input("nhập tiêu đề: ")
            tac_gia = input("nhập tên tác giả: ")
            nam_sang_tac = input("Nhập năm sáng tác: ")
            with open("lab_7_3.csv", "a", encoding="utf") as bai3:
                file = csv.writer(bai3)
                file.writerow([tieu_de, tac_gia, nam_sang_tac])
    print("Đã tạo file và nhập dữ liệu")
except FileExistsError:
    print("file đã tồn tại")
