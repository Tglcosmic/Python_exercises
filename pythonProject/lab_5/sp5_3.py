class SanPham:
    __tensp = ""
    __giasp = ""
    __giamgia = ""

    #Phuong thuc lop
    def setTensp(self, tensanpham):
        self.__tensp = tensanpham

    def getTensp(self):
        return self.__tensp

    def setGiasp(self, giasanpham):
        self.__giasp = giasanpham

    def getGiasp(self):
        return self.__giasp

    def setGiamgia(self, Giamgia):
        self.__giamgia = Giamgia

    def getGiamgia(self):
        return self.__giamgia

    def tinhthue(self):
        return self.__giasp * 0.1

    def nhap(self):
        print("--thông tin sản phẩm--")
        self.setTensp(input("Nhap ten san pham: "))
        self.setGiasp(int(input("Nhap gia san pham: ")))
        self.setGiamgia(int(input("Nhap san gia duoc giam: ")))

    def xuatinf(self):
        print("Ten san pham:", self.getTensp())
        print("Gia san pham:", self.getGiasp())
        print("Gia san pham duoc giam:", self.getGiamgia())
        print("thue sp:", self.tinhthue())

sp1 = SanPham()
sp1.nhap()
sp1.xuatinf()