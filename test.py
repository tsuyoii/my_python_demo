# print(1000000)
# import keyword
# keyword.kwlist

# if 3<5:
#     print(True)
# else:
#     print(False,'hahah')
# print('kkk')

import sys
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if counter>n:
            return
        yield a
        a,b = b,a+b
        counter+=1

f = fibonacci(10)

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# while next(f):
#     try:
#         print(next(f))
#     except StopIteration:
#         sys.exit()

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        print('hh')
        break

