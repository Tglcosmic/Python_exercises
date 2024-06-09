import numpy as np

# Bài 2:
# Sử dụng mảng NumPy trong python để lưu trữ danh sách các cuốn sách (dạng gọi hàm) vớicác yêu cầu:
books = []
#  Thêm mới: Thêm một cuốn sách mới vào danh sách.
def add_book(title):
    books.append(title)
    print("Cuốn sách '{}' đã được thêm mới thành công.".format(title))
#  Xóa: Xóa một cuốn sách khỏi danh sách dựa trên chỉ mục hoặc tên của sách.
def remove_book(index_or_title):
    if isinstance(index_or_title, int):  # Nếu index_or_title là một số nguyên, xóa sách theo chỉ mục
        if 0 <= index_or_title < len(books):
            removed_book = books.pop(index_or_title)
            print("Cuốn sách '{}' đã được xóa thành công.".format(removed_book))
        else:
            print("Chỉ mục không hợp lệ.")
    else:  # Nếu index_or_title không phải là một số nguyên, xóa sách theo tên
        if index_or_title in books:
            books.remove(index_or_title)
            print("Cuốn sách '{}' đã được xóa thành công.".format(index_or_title))
        else:
            print("Không tìm thấy cuốn sách có tên '{}' trong danh sách.".format(index_or_title))
#  Hiển thị: Hiển thị toàn bộ danh sách các sách đã nhập
def display_books():
    print("Danh sách các sách đã nhập:")
    for i, book in enumerate(books):
        print("{}. {}".format(i+1, book))

add_book("jjk")
add_book("Doraemon")
add_book("Naruto")
display_books()
remove_book("Conan")
display_books()