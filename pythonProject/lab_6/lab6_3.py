from lab6_2_6_3 import SinhVienPoly
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
