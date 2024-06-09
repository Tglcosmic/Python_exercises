#Tạo hàm def tính nguyên liệu đường và đậu, trả về giá trị là nguyen_lieu
def tinh_nguyen_lieu(bdx, btc, bd):
    sugar = bdx * 0.04 + btc * 0.06 + bd * 0.05
    bean = bdx * 0.07 + btc * 0 + bd * 0.02

    nguyen_lieu = {"sugar": sugar, "bean": bean}

    return nguyen_lieu

# Dùng hàm map kết hợp với input để nhập nhiều dữ liệu, và xuất ra bằng print
# bdx, btc, db = map(int, input("Nhập số lượng bánh cách nhau bởi dấu phẩy (bánh đậu xanh, bánh thập cẩm, bánh dẻo): ").split(","))
# print(f"Nguyên liệu của bánh là: {tinh_nguyen_lieu(bdx, btc, db)}")
