import numpy as np

# Tạo mảng cấu trúc gồm 3 cột: tên( chuỗi), tuổi(số nguyên), điểm số(số thực)
dtype = np.dtype([('name', 'U50'), ('age', int), ('score', float)])
#Thông tin 3 người vào mảng
data = np.array([('Duc', 21, 87.5), ('Thanh', 26, 92.3), ('Quy', 31, 78.9)], dtype=dtype)
print("Mảng cấu trúc:")
print(data)

#In thông tin người có điểm cao nhất
max_score_index = np.argmax(data['score'])
# In thông tin của người có điểm số cao nhất
print("Thông tin của người có điểm số cao nhất:")
print("Tên:", data['name'][max_score_index])
print("Tuổi:", data['age'][max_score_index])
print("Điểm số:", data['score'][max_score_index])

#Tính và in tuổi trung bình của tất cả mọi người
average_age = np.mean(data['age'])
print("Tuổi trung bình của tất cả mọi người:", average_age)

#Lọc và in thông tin người có tuổi >25( dùng masking)
age_make = data['age'] > 25
filtered_data = data[age_make]
print("Thông6666666665 tin của những người có tuổi lớn hơn 25:")
for person in filtered_data:
    print("Tên:", person['name'])
    print("Tuổi:", person['age'])
    print("Điểm số:", person['score'])
    print()

#cập nhật tên của người đầu tiên trong danh sách thành tên của bạn
data['name'][0] = 'BaChuChiMong'
print("Danh sách sau khi cập nhật:")
print(data)

#Cộng thêm 0.5 điểm cho 'điểm số' nếu 'tuổi' lốn hơn 25
data['score'][age_make] += 0.5
print("Danh sách sau khi cập nhật:")
print(data)

#Bài 2:
#Thêm mới: thêm một môn học mới vào danh sách
# Định nghĩa cấu trúc mới với thêm một cột là 'subject'
new_dtype = np.dtype([('name', 'U50'), ('age', int), ('score', float), ('subject', 'U50')])

# Tạo mảng dữ liệu mới với cấu trúc mới
new_data = np.empty(data.shape, dtype=new_dtype)

# Copy dữ liệu từ mảng cũ sang mảng mới
for field in data.dtype.fields:
    new_data[field] = data[field]

# Thêm thông tin về môn học cho mỗi người trong mảng mới
new_data['subject'] = ['Math', 'Physics', 'Chemistry']

# In ra mảng mới
print("Mảng cấu trúc mới:")
print(new_data)

#xoá một môn học khỏi danh sách dựa trên chỉ mục hoặc tên của môn học
# index_to_delete = 1  # Ví dụ: muốn xóa môn học tại chỉ mục 1
# data_after_deletion = np.delete(data, index_to_delete)
#
# print("Mảng sau khi xóa dựa trên chỉ mục:")
# print(data_after_deletion)

# Xóa môn học dựa trên tên của môn học
subject_to_delete = 'Chemistry'
mask = new_data['subject'] != subject_to_delete
data_after_deletion = data[mask]

print("\nMảng sau khi xóa dựa trên tên môn học:")
print(data_after_deletion)

# Hiển thị toàn bộ danh sách môn học
subjects = np.unique(new_data['subject'])
print("Danh sách môn học:")
for subject in subjects:
    print(subject)