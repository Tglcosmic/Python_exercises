# Hàm để xác định xếp loại dựa trên điểm
def xep_loai(diem):
    if diem < 5:
        return "Yếu"
    elif 5 <= diem < 7:
        return "Trung bình"
    elif 7 <= diem < 8:
        return "Khá"
    elif 8 <= diem < 9:
        return "Giỏi"
    else:
        return "Xuất sắc"

# Khởi tạo danh sách sinh viên khi các bảng sinh viên được nhập sẽ lưu vào danh sách
danh_sach_sinh_vien = []
# hàm range để giới hạn số sinh viên muốn nhập và sau khi nhập các thông tin của sinh viên sẽ lưu vào bảng nhỏ "sinh_vien"
#dùng append để nối bảng "sinh_vien" vào danh_sach_sinh_vien (dùng float để input điểm vì dấu '<' không được hỗ trợ
# hàm int và str)
so_sinh_vien = int(input("nhập số lượng sinh viên: "))
for i in range(so_sinh_vien):
    sinh_vien  = {}
    sinh_vien ['ho_ten'] = input(f"Nhập họ tên sinh viên {i+1}: ")
    sinh_vien ['diem'] = float(input(f"Nhập điểm của sinh viên {i+1}: "))
    sinh_vien ['xep_loai'] = xep_loai(sinh_vien['diem'])
    danh_sach_sinh_vien.append(sinh_vien)

# Xuất thông tin của từng sinh viên ra màn hình
print("\n Thông tin sinh viên:")
for sinh_vien in danh_sach_sinh_vien:
    print(f"\n Họ tên: {sinh_vien['ho_ten']}")
    print(f" điểm: {sinh_vien['diem']}")
    print(f" Xếp loại: {sinh_vien['xep_loai']}")
