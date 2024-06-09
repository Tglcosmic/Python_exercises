import lab4_1 #import file từ bài 4_1
import lab4_2 #import file từ bài 4_2
import lab4_3
def menu(): #Tạo một màn hình menu
    print("+-------------------------+")
    print("1. Tính tiền nước sinh hoạt")
    print("2. Tính nguyên liệu làm")
    print("3. Tìm số chẵn từ dãy số nguyên")
    print("0. Kết thúc")
    print("+-------------------------+")
def cn1():
    so_nuoc, thang = map(int, input("nhập số nước và số tháng cách nhau bởi dấu phẩy: ").split(","))
    print(f"tháng {thang} có số nước là {so_nuoc} với tổng tiền là {lab4_1.tinhtiennuoc(so_nuoc)}")

choice = 1
while choice != 0:
    menu()
    choice = int(input("Hãy chọn giá đúng: "))
    if choice == 0:
        print('Kết thúc chương trình')
        break
    elif choice == 1:
        print("bài 1")
        cn1()
    elif choice == 2:
        print("bài 2")
        bdx, btc, db = map(int, input("Nhập số lượng bánh cách nhau bởi dấu phẩy(bánh đậu xanh, bánh thập cẩm, bánh dẻo): ").split(","))
        print(f"Nguyên liệu của bánh là: {lab4_2.tinh_nguyen_lieu(bdx, btc, db)}")
    elif choice == 3:
        print("bài 3")
        # import lab4_3 #import từ bài 4_3 nhưng không khuyến khích làm cách này vì dễ gây lỗi
        lab4_3.lab_4_3()
    else:
        print("Nước đi này sai cho bạn đi lại")