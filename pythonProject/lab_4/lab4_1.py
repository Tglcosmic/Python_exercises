#Tạo 1 list giá bán nước
gia_ban_nuoc = [7500, 8800, 12000, 24000]

def tinhtiennuoc(sonuoc): #Tạo hàm def tính toán giá tiền nước bằng hàm if và trả về gi trị tổng tiền
    if sonuoc <= 10:
        tongtien = sonuoc * gia_ban_nuoc.index(0)
    elif 20 >= sonuoc > 10:
        tongtien = 10 * gia_ban_nuoc[0] + (sonuoc - 10) * gia_ban_nuoc[1]
    elif 30 >= sonuoc > 20:
        tongtien = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + (sonuoc - 20) * gia_ban_nuoc[2]
    else:
        tongtien = 10 * gia_ban_nuoc[0] + 10 * gia_ban_nuoc[1] + 10 * gia_ban_nuoc[2] + (sonuoc - 30) * gia_ban_nuoc[3]
    return tongtien

# #Tạo hàm giá trị input và output (sử dụng map chp phép nhập nhiều giá trị input với kiểu cùng kiểu dữ liệu)
# so_nuoc, thang = map(int, input("nhập số nước và số tháng cách nhau bởi dấu phẩy: ").split(","))
# print(f"tháng {thang} có số nước là {so_nuoc} với tổng tiền là {tinhtiennuoc(so_nuoc)}")