class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def get_ChuVi(self):
        return (self.dai + self.rong) * 2

    def get_DienTich(self):
        return self.dai * self.rong

    def Nhap(self):
        self.dai = int(input("Nhập chiều dài: "))
        self.rong = int(input("Nhập chiều rộng: "))

    def Xuat(self):
        print("Hình vuông có chiều dài là {} và chiều rộng là {} với Chu vi là {} và Diện tích là {} ".format(self.dai, self.rong, self.ChuVi(), self.DienTich()))

class Vuong(ChuNhat):
    def __init__(self, canh):
        self.canh = canh
        super().__init__(canh, canh)

    def Nhap(self):
        self.canh = int(input("Nhập chiều dài của cạnh vuông:"))

    def Xuat(self):
        print("Hình vuông có cạnh là {} với Chu vi là {} và Diện tích là {} ".format(self.canh, self.ChuVi(), self.DienTich()))

cn1 = ChuNhat("", "")
cn1.Nhap()
cn1.Xuat()

v = Vuong("")
v.Nhap()
v.Xuat()