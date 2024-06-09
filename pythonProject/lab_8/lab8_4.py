import statistics

with open("random_numbers.txt", "r") as file:
    data = file.read().split()

data = [int(num) for num in data]

mean = statistics.mean(data)

std_deviation = statistics.stdev(data)

print("Trung bình của bộ dữ liệu:", mean)
print("Độ lệch chuẩn của bộ dữ liệu:", std_deviation)
