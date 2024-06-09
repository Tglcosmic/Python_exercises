#import test3
#test3.menu()

#print(test3.tinhtoan(4, 0))

my_list = (1, 2, 3, 4, 5)
def bp(x):
    return x*x
list_bp = map(lambda x: x*x, my_list)
for x in list_bp:
    print(x)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)