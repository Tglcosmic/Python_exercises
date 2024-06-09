# a. Tạo dictionary cho thông tin sinh viên
def create_student():
    student_info = {
        "Tên:": input("Nhập tên sinh viên: "),
        "Nam Sinh:": input("Nhập năm sinh: "),
        "Lớp:": input("Nhập lớp: "),
        "Kết Qua Học tập": {
            "Toán:": input("Nhập điểm Toán: "),
            "Lý:": input("Nhập điểm Lý: "),
            "Hóa:": input("Nhập điểm Hóa: ")
        }
    }
    return student_info

# b. Nhập số lượng sinh viên và lưu vào list
num_students = int(input("Nhập số lượng sinh viên: "))
student_list = []

for _ in range(num_students):
    student = create_student()
    student_list.append(student)

# Xuất danh sách sinh viên
print("\nDanh sách sinh viên:")
for idx, student in enumerate(student_list, 1):
    print(f"\nThông tin sinh viên {idx}:")
    for key, value in student.items():
        if type(value) == dict:
            print(f"  {key}:")
            for subject, score in value.items():
                print(f"    {subject}: {score}")
        else:
            print(f"  {key}: {value}")
