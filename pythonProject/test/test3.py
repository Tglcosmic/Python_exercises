# định nghĩa một hàm
def menu():
    print("Menu chương trình")
    print("Cn1")
    print("Cn2")
    print("Cn3")
# gọi hàm
menu()
def tinhtoan(a,b):
    tong = a + b
    hieu = a - b
    nhan = a * b
    chia = a / b
    return tong, hieu, nhan, chia
def hoten(ten):
    ten = input("Nguyễn " +ten)
def tinhtong(*so):
    return sum(so)

print(tinhtoan(3,4 ))

print(hoten("huỳnh"))

print(tinhtong(1, 2, 3))
print(tinhtong(1, 2, 3, 4, 5))

x = lambda a, b: a + b
print(x(2, 3))

check = lambda x: True if x % 2 == 0 else False
print(check(10))