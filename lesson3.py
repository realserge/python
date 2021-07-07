# 1.
# def division(arg1, arg2):
#     try:
#         res = arg1/arg2
#     except ZeroDivisionError:
#         return
#     return res
# arg1= float(input("Введите делимое: "))
# arg2= float(input("Введите делитель: "))
# res= division(arg1, arg2)
# if  res:
#     print(res)
# else:
#     print(f"Деление на ноль {arg1}/{arg2}")
# 2.
# def user(name, surname, year_of_birth, city, email, phone):
#     s= [name, surname, year_of_birth, city, email, phone]
#     return " ".join(s)
# name= input("Введите имя: ")
# surname= input("Введите фамилию: ")
# year_of_birth= input("Введите год рождения: ")
# city= input("Введите город проживания: ")
# email= input("Введите эл. адрес: ")
# phone= input("Введите телефон: ")
# result= user(phone= phone,email= email, city= city, name= name, surname= surname, year_of_birth= year_of_birth )
# print(result)
# 3.
# def my_func(a,b,c):
#     s= [a, b, c]
#     s.remove(min(s))
#     return sum(s)
# a= 6
# b= 8
# c= 3
# print(my_func(a, b, c))
# 4.
# def  my_func(x, y):
#
#     v.1
#     return x ** y
#     v.2
#     res = x
#     for i in range(abs(y) - 1):
#         res = res * x
#     return 1 / res
# x= float(input("Введите действительное положительное число: "))
# y= int(input("Введите целое отрицательное число: "))
# print("x в степени y = ",my_func(x,y))
# 5.
# res = 0
# doing = 1
# while doing:
#     i = input("Введите цифры через пробел: ")
#     i = i.split()
#     a = 0
#     while a<len(i):
#         try:
#             i[a] = int(i[a])
#             res = res + i[a]
#
#         except ValueError:
#             print("расчет окончен")
#             doing = 0
#             break
#         a = a + 1
#     print(res)
# 6.
# def int_func(string):
#     return  string.capitalize()
#
# i = input("Введите слова: ")
# i = i.split()
# a=0
# out_str = " "
# while a<len(i):
#     i[a]= int_func(i[a])
#     a = a + 1
# print(out_str.join(i))

