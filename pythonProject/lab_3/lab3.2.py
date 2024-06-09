#sử dụng hàm def để tạo ra xếp loại điểm
def xep_loai(diem):
    if diem < 5:
        return "yếu"
    elif 5 <= diem < 7:
        return "trung bình"
    elif 7 <= diem <8:
        return "khá"
    elif 8<= diem < 9:
        return "giỏi"
    else:
        return "xuất sắc"

#tạo ra biến rỗng để chứa các biến về sau
sinh_vien = {}

#tạo biến từ input
sinh_vien["họ tên"] = input("Nhập họ tên sinh viên: ")
sinh_vien["điểm"] = float(input("nhập điểm của sinh viên: "))

#tạo biến lấy dữ liệu từ biến của hàm def
sinh_vien["xếp loại"] = xep_loai(sinh_vien['điểm'])

#in các thông tin
print("thông tin cá nhân")
print("họ tên: ", sinh_vien['họ tên'])
print("điểm: ", sinh_vien["điểm"])
print("xếp loại: ", sinh_vien["xếp loại"])  