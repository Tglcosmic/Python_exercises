full_name = input("Nhập họ và tên: ")
name_parts = full_name.split()
last_name = name_parts[0].upper()
first_name = name_parts[-1].upper()
middle_name = ' '.join(name_parts[1:-1])

print("Họ:", last_name)
print("Tên đệm:", middle_name)
print("Tên:", first_name)
