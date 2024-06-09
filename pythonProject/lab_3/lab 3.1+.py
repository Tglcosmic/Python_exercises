#sử dụng kiểu list, hàm for với mỗi phần tử được nhập cách nhau bởi dấu phẩy để nhập dãy số
day_so = [int(x) for x in input("Nhập dãy số bất kì cách nhau bởi dấu phẩy: ").split(",")]

#sắp xếp dãy số theo chiều giảm dần và in nó ra
#(hàm reverse sẽ đảo chiều các phần tử trong list với đk True)
day_so.sort(reverse=True)
min_day_so = day_so[-1]
print(day_so)
print("phần tử có giá trị nhỏ nhất là: ", min_day_so)
