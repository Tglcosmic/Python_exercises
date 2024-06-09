import numpy as np

# 1. Tạo một mảng cấu trúc có 3 cột: 'name', 'age', 'score'
dtype = [('name', 'U10'),
         ('age', int),
         ('score', float)]
people = np.array([('John', 25, 78.5), ('Emma', 30, 85.0), ('Michael', 22, 80.3)], dtype=dtype)

# 2. In ra thông tin của người có điểm số cao nhất
max_score_index = np.argmax(people['score'])
print("Thông tin của người có điểm số cao nhất:")
print("Name:", people[max_score_index]['name'])
print("Age:", people[max_score_index]['age'])
print("Score:", people[max_score_index]['score'])

# 3. Tính và in ra tuổi trung bình của tất cả người trong mảng
average_age = np.mean(people['age'])
print("Tuổi trung bình của tất cả người trong mảng:", average_age)

# 4. Sử dụng masking để lọc ra các người có tuổi lớn hơn 25 và in ra thông tin của họ
mask = people['age'] > 25
people_over_25 = people[mask]
print("Thông tin của những người có tuổi lớn hơn 25:\n", people_over_25)
