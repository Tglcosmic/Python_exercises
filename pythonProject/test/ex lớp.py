#input
nhap = input("nhập dữ liệu: ")

#dùng split để tách input thành dạng list dựa trên kí tự cho trước VD: hello.com => ['hello', 'com']
tach = nhap.split(".")

#lưu tạm thời phần tử dưới cùng
list = []
list.append(tach[-1])

#dùng if để in ra phần tử có phần mở rộng
if len(tach) > 1:
    print(f"Dữ liệu vừa là {nhap} có tệp mở rộng là {list}")
else:
    print("không xác định")

#cách khác
# Nhập tên tập tin từ người dùng
#ten_tap_tin = input("Nhập tên của tập tin: ")

# Tách phần mở rộng từ tên tập tin
#phan_mo_rong = ten_tap_tin.split('.')[-1]

# Xuất phần mở rộng
#if len(phan_mo_rong) > 0:
#    print(f"Phần mở rộng của tập tin {ten_tap_tin}: {phan_mo_rong}")
#else:
#    print(f"Tập tin {ten_tap_tin} không có phần mở rộng.")
