import numpy as np

# Nhập số lượng sinh viên từ bàn phím
num_students = int(input("Nhập số lượng sinh viên: "))

# Khởi tạo mảng cấu trúc
dtype = [('name', 'U10'), ('age', int), ('score', float)]
students_array = np.zeros(num_students, dtype=dtype)

# Nhập thông tin của từng sinh viên và kiểm tra tính hợp lệ
for i in range(num_students):
    name = input("\nNhập tên của sinh viên: ")

    while True:
        age = int(input("Nhập tuổi của sinh viên: "))
        if age < 0:
            print("Tuổi không hợp lệ vui lòng nhập lại!")
            continue
        else:
            break
    while True:
        score = float(input("Nhập điểm số của sinh viên: "))
        if score < 0 or score > 10:
            print("Điểm không hợp lệ vui lòng nhập lại!")
            continue
        else:
            break
    students_array[i] = (name, age, score)
# Thông tin tất cả sinh viên vừa nhập
print("\nThông tin của sinh viên:")
print("{:<17}{:<7}{:<3}".format("Họ và Tên", "Tuổi", "Điểm"))
for student in students_array:
    print("{:<17}{:<7}{:<3}".format(student['name'], student['age'], student['score']))

# In ra thông tin của sinh viên có điểm số cao nhất
max_score_student = students_array[np.argmax(students_array['score'])]
print("\nThông tin của sinh viên có điểm số cao nhất:")
print("{:<17}{:<7}{:<3}".format(("Họ và Tên"), ("Tuổi"), ("Điểm")))
print("{:<17}{:<}7{:<3}".format(max_score_student['name'], max_score_student['age'], max_score_student['score']))
# Tính và in ra tuổi trung bình của tất cả sinh viên
average_age = np.mean(students_array['age'])
print("\nTuổi trung bình của tất cả sinh viên:", average_age)

# Lọc ra thông tin của sinh viên có tuổi lớn hơn 25
students_over_25 = students_array[students_array['age'] > 25]
print("\nThông tin của những sinh viên có tuổi lớn hơn 25:")
print("{:<17}{:<7}{:<3}".format("Họ và Tên", "Tuổi", "Điểm"))
for student in students_over_25:
    print("{:<17}{:<7}{:<3}".format(student['name'], student['age'], student['score']))
