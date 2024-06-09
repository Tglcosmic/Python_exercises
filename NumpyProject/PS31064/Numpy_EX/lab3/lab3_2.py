import numpy as np

ls_subject = np.array([])
def add_subject(subject):
    global ls_subject
    ls_subject = np.append(ls_subject, subject)
    print(f"Đã thêm môn học {subject}.")
def del_subject(subject):
    global ls_subject
    idx = np.where(ls_subject == subject)[0]  # Trích xuất chỉ mục từ tuple
    if len(idx) > 0:
        ls_subject = np.delete(ls_subject, idx)
        print(f"Đã xóa môn học {subject}.")
    else:
        print(f"Môn học '{subject}' không tồn tại trong danh sách.")
def deleted_monhoc(subject):
    try:
        subject_index = int(subject)
        if 0 <= subject_index < len(ls_subject):
            del_subject(ls_subject[subject_index])
        else:
            print("Chỉ mục môn học không hợp lệ.")
    except ValueError:
        del_subject(subject)
def display_ls_subject():
    print("Danh sách các môn học:")
    print("{:<5}{:<15}".format("STT", "Môn học"))
    for idx, subject in enumerate(ls_subject):
        print("{:<5}{:<15}".format(idx, subject))
while True:
    print("\n------ MENU ------")
    print("1. Thêm môn học")
    print("2. Xóa môn học")
    print("3. Hiển thị danh sách môn học")
    print("4. Thoát")
    choice = input("Chọn chức năng (1-4): ")
    if choice == '1':
        new_subject = input("Nhập tên môn học mới: ")
        add_subject(new_subject)
    elif choice == '2':
        subject = input("Nhập chỉ mục môn học hoặc tên môn học cần xóa: ")
        deleted_monhoc(subject.lower())
    elif choice == '3':
        display_ls_subject()
    elif choice == '4':
        print("Đã thoát chương trình, cám ơn bạn đã sử dụng dịch vụ này")
        break
    else:
        print("Nhập sai lựa chọn rồi bạn ơi. Nhập lại đê")
