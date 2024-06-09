def tao_ma_id():
    global current_id
    max_ma_id = 0
    with open("hehe", "r", encoding="utf-8") as file:
        for line in file:
            ma_id = line.strip().split(',')[0]
            if ma_id.startswith("PS") and ma_id[2:].isdigit():
                ma_id = int(ma_id[2:])
                if ma_id > max_ma_id:
                    max_ma_id = ma_id
    current_id = max_ma_id + 1
    return f"PS{current_id:05d}"

# Sử dụng hàm để tạo mã ID tự động
auto_id = tao_ma_id()
print(auto_id)
