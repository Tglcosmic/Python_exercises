n = int(input("nhập vào số tự nhiên n ( 0 < n < 10): "))

if 0 < n < 10:
    result = n + int(str(n) * 2) + int(str(n) * 3) + int(str(n) * 4)
    print(f'kết quả của {n} + {n}{n} + {n}{n}{n}+ {n}{n}{n}{n} là : {result}')
else:
    print('bạn đã nhập sai vui lòng tra goole xem số tự nhiên 0 < n < 10 là số mấy rồi nhập lại')
    print("PS: pycharm đã quạo '^'!")