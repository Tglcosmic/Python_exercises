class NhanVien:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def get_Thu_Nhap(self):
        return self.salary

class TiepThi(NhanVien):
    def __init__(self, id, name, salary, commission, sales):
        NhanVien.__init__(self, id, name, salary)
        self.sales = sales
        self.commission = commission

    def get_Thu_Nhap(self):
        return self.salary + self.sales * self.commission

class TruongPhong(NhanVien):
    def __init__(self, id, name, salary, allowance):
        NhanVien.__init__(self, id, name, salary)
        self.allownce = allowance

    def get_Thu_Nhap(self):
        return self.salary + self.allownce
