# try:
#     fileopen = open("demo_ca_1.txt", mode="r", encoding="utf8")
# except FileNotFoundError:
#     print("không thấy bạn ơi")

# # Mở file
# fileopen = open("demo_ca_1.txt", mode='a', encoding="utf")
#
# # Ghi dữ liệu
# data = input("Nhap du lieu: ")
# fileopen.write(data)
#
# # Đóng file
# fileopen.close()

# with open("demo_ca_1.txt", mode='r', encoding="utf") as fileopen:
#     date = input("Nhap du lieu: ")
#     fileopen.write(date)

# mở file
# fileopen = open("H:/Python exercises/pythonProject/lab_7/DAT201-Lab_7-Resource.txt", mode='r', encoding="utf8")

# # đọc file
# data = fileopen.readline()
# data2 = fileopen.readline()
# print(data)
# print(data2)
#
# # đóng file
# fileopen.close()

# Mở file

fileopen = open("/lab_7/DAT201-Lab_7-Resource.txt", mode='r', encoding="utf8")
# Đọc nội dung của file
content = fileopen.read()

# Thực hiện thay thế từ "quê hương" thành "đất mẹ"
new_content = content.replace("quê hương", "đất mẹ")

# In ra nội dung mới đã thay thế
print("Nội dung mới sau khi thay thế:")


# Ghi nội dung mới vào file
fileopen = open("/lab_7/DAT201-Lab_7-Resource.txt", mode='w', encoding="utf8")
fileopen.write(new_content)
print(new_content)
