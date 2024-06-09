with open("DAT201-Lab_7-Resource.txt", encoding="utf-8") as L7:
    NoiDung = L7.read()
    print("Noi dung file la: ")
    print(NoiDung)
    L7.seek(0)

    TenBaiTho = L7.readline().strip()[:9]
    print("\n ten bai tho: ")
    print(TenBaiTho)

    TenTacGia = L7.readline().strip()
    print("\n Ten tac gia: ")
    print(TenTacGia)
