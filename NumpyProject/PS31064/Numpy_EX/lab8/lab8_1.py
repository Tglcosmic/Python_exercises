import numpy as np

# Bước 1: Tạo mảng NumPy chứa thời gian phục vụ của các đơn hàng
thoi_gian_phuc_vu = np.random.randint(1, 60, 15)
print(thoi_gian_phuc_vu)

# Bước 2: Tính và in ra thời gian phục vụ trung bình
thoi_gian_trung_binh = np.mean(thoi_gian_phuc_vu)
print("Thời gian phục vụ trung bình:", thoi_gian_trung_binh, "phút")

# Bước 3: Tìm và in ra phần trăm thời gian phục vụ dưới 15 phút
pham_tram_duoi_15_phut = np.mean(thoi_gian_phuc_vu < 15) * 100
print(f"Thời gian phục vụ dưới 15: {len(thoi_gian_phuc_vu[thoi_gian_phuc_vu < 15])}")
print("Phần trăm thời gian phục vụ dưới 15 phút:", pham_tram_duoi_15_phut, "%")

# Bước 4: Tính và in ra độ lệch chuẩn của dữ liệu thời gian phục vụ
do_lech_chuan = np.std(thoi_gian_phuc_vu)
print("Độ lệch chuẩn của thời gian phục vụ:", do_lech_chuan)


