import re

txt = "Cao đẳng FPT Polytechnic HCM cao dẳng sài gon"

# hàm findall

x = re.findall("ao", txt)
#
y = re.search(r'\s', txt)

z = re.split(r'\s', txt)

t = re.sub(r'\s',"_", txt)


print(x)
print(y.start())
print(y.end())
print(z)
print(t)