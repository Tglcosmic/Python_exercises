class ChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def get_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def get_dien_tich(self):
        return self.dai * self.rong

    def xuat(self):
        print("Chiều dài:", self.dai)
        print("Chiều rộng:", self.rong)
        print("Diện tích:", self.get_dien_tich())
        print("Chu vi:", self.get_chu_vi())

class Vuong(ChuNhat):
    def __init__(self, canh):
        ChuNhat.__init__(self, canh, canh)

    def xuat(self):
        print("Cạnh:", self.dai)  # Vì là vuông nên chiều dài = chiều rộng = cạnh
        print("Diện tích:", self.get_dien_tich())
        print("Chu vi:", self.get_chu_vi())

# Nhập dữ liệu
def in_out():
    dai_cn1 = float(input("Nhập chiều dài hình chữ nhật 1: "))
    rong_cn1 = float(input("Nhập chiều rộng hình chữ nhật 1: "))
    dai_cn2 = float(input("Nhập chiều dài hình chữ nhật 2: "))
    rong_cn2 = float(input("Nhập chiều rộng hình chữ nhật 2: "))
    canh_vuong = float(input("Nhập cạnh hình vuông: "))

    # Tạo đối tượng và xuất thông tin
    cn1 = ChuNhat(dai_cn1, rong_cn1)
    cn2 = ChuNhat(dai_cn2, rong_cn2)
    vu = Vuong(canh_vuong)

    print("Thông tin hình chữ nhật 1:")
    cn1.xuat()
    print("\nThông tin hình chữ nhật 2:")
    cn2.xuat()
    print("\nThông tin hình vuông:")
    vu.xuat()
in_out()

