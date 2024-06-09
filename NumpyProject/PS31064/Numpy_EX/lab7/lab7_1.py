import numpy as np

# Tạo mảng NumPy chứa 10 số nguyên ngẫu nhiên trong khoảng từ 1 đến 100
arr = np.random.randint(1, 101, 10)
print(f"Mảng ban đầu: {arr}")

# 1. Tính và in ra giá trị trung bình của các phần tử trong mảng
print("Giá trị trung bình của các phần tử trong mảng là:", np.mean(arr))

# 2. Sắp xếp mảng theo thứ tự tăng dần và in ra kết quả
print("Mảng sau khi được sắp xếp theo thứ tự tăng dần:", np.sort(arr))

# 3. Tạo một chuỗi từ các phần tử trong mảng (dạng chuỗi có định dạng) và in ra chuỗi này
string_arr = ' '.join(map(str, arr))
print("Chuỗi từ các phần tử trong mảng:", string_arr)

# 4. Tính và in ra tổng các số nguyên tố có trong mảng
prime_elements = [x for x in arr if all(x % i for i in range(2, x)) and x > 1]
print("Tổng các số nguyên tố có trong mảng là:", np.sum(prime_elements))

# 5. In ra số lần xuất hiện của từng phần tử duy nhất trong mảng
print("Số lần xuất hiện của từng phần tử duy nhất trong mảng:")
unique_elements, counts = np.unique(arr, return_counts=True)
for element, count in zip(unique_elements, counts):
    if count > 1:
        print(f"{element}: {count} lần")