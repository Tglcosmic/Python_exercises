try:
    with open("DAT201-Lab_7-Resource.txt", "r", encoding="utf-8") as file:
        poem_lines = file.readlines()
        poem_title = poem_lines[0].strip()
        poet_name = poem_lines[1].strip()

        # Chia mỗi đoạn thơ thành các phần nhỏ hơn
        sections = []
        for i in range(2, len(poem_lines), 5):
            section = " ".join([line.strip() for line in poem_lines[i:i + 5]])
            sections.append(section)

    with open("poem.xml", "w", encoding="utf-8") as xml_file:
        xml_file.write("<songs>\n")
        xml_file.write("\t<song>\n")
        xml_file.write("\t\t<name>" + poem_title + "</name>\n")
        xml_file.write("\t\t<author>" + poet_name + "</author>\n")

        # Ghi từng đoạn thơ vào file XML
        for section in sections:
            xml_file.write("\t\t<section>" + section + "</section>\n")

        xml_file.write("\t</song>\n")
        xml_file.write("</songs>")

    print("Đã ghi dữ liệu vào file poem.xml")

except FileNotFoundError:
    print("Không tìm thấy file DAT201 - Lab 7 – Resource.txt")
except Exception as e:
    print("Đã xảy ra lỗi:", e)
