import sp5_4

sp1 = sp5_4.SanPham("",  "", "")
sp2 = sp5_4.SanPham("", "", "")

print("--Nhập thông tin sản phẩm--")
sp1.nhap()
print("--Nhập thông tin sản phẩm--")
sp2.nhap()
print("============================")

print("Thông tin sản phẩm 1")
sp1.xuatinf()
print("Thông tin sản phẩm 2")
sp2.xuatinf()
