import numpy as np

# Tạo một mảng NumPy chứa dữ liệu quảng cáo (0 - không xem, 1 - đã xem).
ADS = np.random.randint(0, 2, 16)

# Tạo một mảng tương ứng xác định liệu khách hàng có mua sản phẩm hay không (0 - không mua, 1 - đã mua).
PCh = np.random.randint(0, 2, 16)

# Tính tỷ lệ khách hàng mua sản phẩm sau khi xem quảng cáo.
print(f"Xem: {ADS}, số lần xem {np.count_nonzero(ADS)}")
print(f"Mua: {PCh}, số lần mua {np.count_nonzero(PCh)}")

print(f"Xem mua {np.logical_and(ADS, PCh)}")

arr_xemMua = np.count_nonzero(np.logical_and(ADS, PCh))
print(f"Mua sau khi xem: {(arr_xemMua / np.count_nonzero(ADS)) * 100} %")

arr_xemKMua = np.count_nonzero(np.logical_and(ADS, np.logical_not(PCh)))
print(f"không mua sau khi xem: {(arr_xemKMua / np.count_nonzero(ADS)) * 100} %")


from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# 5. Tính ma trận confusion và in ra các chỉ số đánh giá mô hình (precision, recall, F1-score).
confusion_matrix = confusion_matrix(PCh, ADS)

precision = precision_score(PCh, ADS)
recall = recall_score(PCh, ADS)
f1_score = f1_score(PCh, ADS)

# 6. Đưa ra nhận xét/sự giải thích về hiệu suất dự đoán dữ liệu dựa trên các kết quả thu được.
print("Ma trận confusion:", confusion_matrix)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)
