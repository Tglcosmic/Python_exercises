import datetime

#input
inname = input("nhập tên của bạn: ")
inage = int(input("nhập năm sinh của bạn: "))

#hàm xử lí
day = datetime.date.today()
yn = day.year
age = yn - inage

#output
print(f'bạn tên là :{inname}, năm nay bạn {age} tuổi')