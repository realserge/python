# 1.
# from sys import argv
# hours = float(argv[1])
# stavka = float(argv[2])
# prem = float(argv[3])
# zp = hours * stavka + prem
# print(zp)

# 2.
# my_list = [int(i) for i in input().split()]
# new_list = [ j for i, j in zip(my_list, my_list[1:]) if j > i]
# print(new_list)

# 3.
# my_list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
# print(my_list)

# 4.
# my_list = [int(i) for i in input().split()]
# new_list = [ i for i in my_list  if my_list.count(i) == 1]
# print(new_list)

# 5.
# from functools import reduce
# def xy(x,y):
#     return x * y
# my_list = [i for i in range(100, 1001) if i % 2 == 0 ]
# print(my_list)
# print(reduce(xy,my_list))

# 6.
# a.
# from itertools import count
# x = int(input("Введите число: "))
# for i in count(x):
#     print(i)
# b.
# from itertools import cycle
# for i in cycle(['Белый', 'Синий', 'Красный']):
#     print(i)

# 7.
# from itertools import count
# def fibo_gen():
#     for el in count(1):
#         x = 1
#         for i in range(1,el+1):
#             x *= i
#         yield x
# x = 0
# for i in fibo_gen():
#     if x < 15:
#         print(i)
#         x += 1
#     else:
#         break