def kt(so): # Tạo 1 hàm xác định giá trị có phải là số nguyên hay không (hàm try là hàm sử lý ngoại lệ)
    try: # kiểm tra hàm có thể gây ra ngoại lệ
        int(so)
        return True
    except ValueError: # xử lí khi hàm try báo có ngoại lệ và xử lí hàm đó
        print("không phải số nguyên")
        return False
def lab_4_3():
    my_list = []
    while True: # Sử dụng vòng lặp while để chạy cho đến khi nhập stop để kết thúc
        x = input("Nhập 1 số nguyên bất kì: ")
        if x == "stop":
            print("Kết thúc chương trình")
            break
        elif kt(x) is True:
            my_list.append(int(x))
        elif kt(x) is False:
            print("bạn đã nhập sai, yêu cầu nhập lại")
    new_list = list(filter(lambda x: (x % 2 == 0), my_list))
    print(my_list)
    print('số chẳn là:\n ', new_list)
