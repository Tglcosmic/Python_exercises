# import re
#
# hoten = input("nhập họ và tên: ")
#
# ds_hoten = re.split(r'\s', hoten)
# for x,y in enumerate(ds_hoten):
#     if x == 0 or x == len(ds_hoten)-1:
#         print(ds_hoten[x].upper())
#     else:
#         print(ds_hoten[x])
import re

Sinhvien = {
    "name": " ",
    "email": " ",
    "phone": " ",
    "cccd": " "
}

pattern_cccd = r'[0][0-9]{11}'
pattern_phone = r'[0][1-9][0-9]{8}'
pattern_email = r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z-.]{2,}$'

def check_id(cccd):
    if re.match(pattern_cccd, cccd):
        return True
    else:
        return False

def check_p(phone):
    if re.match(pattern_phone, phone):
        return True
    else:
        return False

def check_e(email):
    if re.match(pattern_email, email):
        return True
    else:
        return False

while True:
    cccd = input("nhap cccd: ")
    if check_id(cccd):
        Sinhvien["cccd"] = cccd
        print('Được rồi bạn ơi')
        break
    else:
        print("sao rồi bạn ơi")

while True:
    phone = input("nhap so dien thoai: ")
    if check_p(phone):
        Sinhvien["phone"] = phone
        print('ok rồi bạn ơi')
        break
    else:
        print("vẫn sai bạn ơi")

while True:
    email = input("nhap email: ")
    if check_e(email):
        Sinhvien["email"] = email
        print('xong rồi kiểm tra lại đi bạn')
        break
    else:
        print("sao lại sai nữa dị bạn ơi")

print(Sinhvien)