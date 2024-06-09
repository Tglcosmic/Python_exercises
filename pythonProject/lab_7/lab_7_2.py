fileopen = open("lab 7 - Resource2.txt", mode="w", encoding="utf8")

poem = '''
“…
Nếu một mai tôi có bay lên trời
Thì người ơi tôi đã sống rất thảnh thơi
Nếu một mai tôi có đi qua đời

Thì người ơi tôi đã sống rất tuyệt vời
…”
'''
fileopen.write(poem)
fileopen.close()
print("Đã lưu vào file Lab7-Exercise2.txt")