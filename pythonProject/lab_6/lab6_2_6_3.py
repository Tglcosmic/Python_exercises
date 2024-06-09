class SinhVienPoly:
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh

    def get_diem(self):
        pass

    def get_hoc_luc(self):
        if self.get_diem() < 5:
            return "Yếu"
        elif 5 <= self.get_diem() < 7:
            return "Trung bình"
        elif 7 <= self.get_diem() < 8:
            return "Khá"
        elif 8 <= self.get_diem() < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def xuat(self):
        print("{:16}{:16}{:8}{:8}".format(self.ho_ten, self.nganh, self.get_diem(), self.get_hoc_luc()))

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, nganh)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def get_diem(self):
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4

class SinhVienBiz(SinhVienPoly):
    def __init__(self, ho_ten, nganh, diem_marketing, diem_sales):
        super().__init__(ho_ten, nganh)
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales

    def get_diem(self):
        return (2 * self.diem_marketing + self.diem_sales) / 3
#
#
# sv_it = SinhVienIT("Nguyễn Văn A", "Công nghệ thông tin", 8, 7, 6)
# sv_biz = SinhVienBiz("Trần Thị B", "Kinh doanh", 8, 8)
# sv_it.xuat()
# sv_biz.xuat()
