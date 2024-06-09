class NhanVien:
    def __init__(self, hoten, luong, ma):
        self.ma = ma
        self.hoten = hoten
        self.luong = luong
    def get_thu_nhap(self):
        pass
    def get_thue(self):
        if self.get_thu_nhap() < 9000:
            return "Không đóng thuế"
        elif self.get_thu_nhap() < 15000:
            return self.get_thu_nhap() * 0.1
        else:
            return self.get_thu_nhap() * 0.15
    def xuat(self):
        print("{:<8} {:<16}{:<8}{:<8}".format(self.ma, self.hoten, self.get_thu_nhap(), self.get_thue()))
    def write(self):
        return ("{:<8} {:<16}{:<8}{:<8}".format(self.ma, self.hoten, self.get_thu_nhap(), self.get_thue()))
class TiepThi(NhanVien):
    def __init__(self, hoten, luong, ma, ds, hh):
        super().__init__(hoten, luong, ma)
        self.ds = ds
        self.hh = hh
    def get_thu_nhap(self):
        return self.luong + (self.ds * (self.hh/100) * 1000)
class TruongPhong(NhanVien):
    def __init__(self, hoten, luong, ma, luongtn):
        super().__init__(hoten, luong, ma)
        self.luongtn = luongtn
    def get_thu_nhap(self):
        return self.luong + self.luongtn