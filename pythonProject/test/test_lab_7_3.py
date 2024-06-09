import os
#
# if os.path.exists("demo_ca_1.txt"):
#     os.remove("demo_ca_1.txt")
# else:
#     print("file không tồn tại")


# # os.rmdir("text_data")
# brands = ("ford","honda","toyota","mazda","kia")
# models = ("wild track","city","hulix","cx 6","santa fee" )
# years = (2019,2020,2021,2022,2023)
# colors =("red", "blue", "black","yellow","orange")
#
#
# try:
#     filename = input("Nhập tên file: ")
#     file1 = open(filename, "x")
# except FileExistsError:
#     print("File tồn tại")
#
# for x in range(5):
#     file1.write("{}, {}, {}, {}\n".format(brands[x], models[x], years[x], colors[x]))
#
# file1.close()
# brands = ("ford","honda","toyota","mazda","kia")
# models = ("wild track","city","hulix","cx 6","santa fee" )
# years = (2019,2020,2021,2022,2023)
# colors =("red", "blue", "black","yellow","orange")
#
#
# try:
#     filename = input("Nhập tên file")
#     file1 = open(filename, "w")
# except FileExistsError:
#     print("File tồn tại")
#
# file1.write("<cars>\n")
# for x in range(5):
#     file1.write("<car>\n")
#     file1.write("<brands> {} </brands>".format(brands[x]))
#     file1.write("<models> {} </models>".format(models[x]))
#     file1.write("<years>  {} </years>".format(years[x]))
#     file1.write("<colors> {} </colors>\n".format(colors[x]))
#     file1.write("</car>\n")
# file1.write("</cars>")
# file1.close()