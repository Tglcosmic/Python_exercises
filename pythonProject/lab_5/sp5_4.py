class SanPham:
    # Thuộc tính của lớp
    # tensp = ""
    # giasp = ""
    # giamgia = ""
    # Phương thức của lớp
    def __init__(self, tensanpham, giasanpham, giamgia):
        self.tensp = tensanpham
        self.giasp = giasanpham
        self.giamgia = giamgia
    def tinhthue(self):
        return self.giasp * 0.1

    def nhap(self):
        self.tensp = input("Nhap ten san pham: ")
        self.giasp = int(input("Nhap gia san pham: "))
        self.giamgia = int(input("Nhap san gia duoc giam: "))

    def xuatinf(self):
        print("Ten san pham:", self.tensp)
        print("Gia san pham:", self.giasp)
        print("Gia san pham duoc giam:", self.giamgia)
        print("thue sp:", self.tinhthue())

# sp1 = SanPham()
# sp1.nhap()
# sp1.xuatinf()