class SinhVien:
    def __init__(self, Ten, Nganh):
        self.Ten = Ten
        self.Nganh = Nganh
    def get_diem(self):
        pass
    def get_hocluc(self):
        diem = self.get_diem()
        if diem < 5:
            return "yếu"
        elif 5 <= diem < 7:
            return "Trung bình"
        elif 7 <= diem < 8:
            return "Khá"
        elif 8 <= diem < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def nhap(self):
        self.Ten = input("Nhập tên sinh viên: ")
        self.Nganh = input("Sinh viên thuộc ngành: ")

    def xuat(self):
        print("Sinh viên {} của ngành {} đạt {} điểm và xếp học lực {}".format(self.Ten, self.Nganh, self.get_diem(), self.get_hocluc()))

class SinhVienIT(SinhVien):
    def __init__(self,Ten, Nganh, diem_java, diem_html, diem_css):
        SinhVien.__init__(self, Ten, Nganh)
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def get_diem(self):
        return (2 * self.diem_java + self.diem_html + self.diem_css) / 4

    def nhap(self):
        SinhVien.__init__(self, self.Ten, self.Nganh)

    def xuat(self):
        print(
            "Sinh viên Biz tên là: {}, ngành {} đạt được {} điểm java, {} điểm html, {} điểm css".format(self.Ten, self.Nganh, self.diem_java, self.diem_html, self.diem_css))



class SinhVienBiz(SinhVien):
    def __init__(self, Ten, Nganh, diem_marketing, diem_sales):
        SinhVien.__init__(self, Ten, Nganh)
        self.diem_marketing = diem_marketing
        self.diem_sales = diem_sales

    def get_diem(self):
        return (2 * self.diem_marketing + self.diem_sales) / 3

    def nhap(self):
        SinhVien.__init__(self, self.Ten, self.Nganh)   

    def xuat(self):
        print("Sinh viên Biz tên là: {}, ngành {} đạt được {} điểm marketing, {} điểm sales".format(self.Ten, self.Nganh, self.diem_marketing, self.diem_sales))