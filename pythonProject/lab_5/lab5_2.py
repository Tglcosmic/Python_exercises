import lab5_1 # import file từ bài 5_1

# Khởi tạo đối tượng
sp1 = lab5_1.SanPham()
sp2 = lab5_1.SanPham()

# Gọi phương thức nhập
print("--Nhập thông tin sản phẩm--")
sp1.nhap()
sp2.nhap()
print("============================")

# Gọi phương thức xuất
print("Thông tin sản phẩm 1")
sp1.xuatinf()
print("\nThông tin sản phẩm 2")
sp2.xuatinf()