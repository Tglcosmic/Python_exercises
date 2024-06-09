class SanPham: #Tạo lớp
    # Thuộc tính của lớp
    tensp = ""
    giasp = ""
    giamgia = ""
    # Phương thức của lớp
    def tinhthue(self):
        return self.giasp * 0.1
    def xuatinf(self):
        print("Tên sản phẩm:", self.tensp)
        print("Giá sản phẩm:", self.giasp)
        print("Giá sản phẩm được giảm:", self.giamgia)
        print("thue sp:", self.tinhthue())
    def nhap(self):
        self.tensp = input("Nhập tên sản phẩm: ")
        self.giasp = int(input("Nhập giá sản phẩm: "))
        self.giamgia = int(input("Giá sản phẩm giảm: "))

#Gọi các phương thức của lớp
# sp1 = SanPham()
# sp1.nhap()
# sp1.xuatinf()