#input chuỗi
chuoi = input("nhập chuỗi kí tự: ")

#tạo biến chứa
ket_qua = {}

#tạo vòng lặp đếm từng kí tự (get sẽ kiểm tra ký tự có trong chuỗi hay không)
#cú pháp: value = dictionary .get(key, default) default: tùy chọn giá trị khi key không tìm thấy
for ky_tu in chuoi:
    ket_qua[ky_tu] = ket_qua.get(ky_tu, 0) + 1

print("Kết quả: ", ket_qua)
