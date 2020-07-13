# 1.
# a = 5
# b = 10
# print(a+b)

# answer = int(input('Введите число: '))
# print(answer)
# answer = input('Введите кодовые слова: ')
# print(answer)
# print(f' {44 :02d}')
# 2.
# time = int(input('Введите время в секундах: '))
# hour = time // 3600
# minut = (time - hour * 3600) // 60
# second = time - hour * 3600 - minut * 60
# print(f" {hour:02d}:{minut:02d}:{second:02d}  чч:мм:сс")
# 3.
#

# num = int(input('Введите число: '))
# result = num + int(str(num)+str(num)) + int(str(num)+str(num)+str(num))
# print(result)
# 4.
# num = int(input('Введите целое положительное число: '))
# maxdigit = num%10
# num = num//10
# while num > 0:
#     if num%10 > maxdigit:
#         maxdigit = num%10
#     num = num//10
# print(maxdigit)
# 5.
# viruchka = int(input('Сообщите выручку: '))
# izderzhki = int(input('Сообщите издержки: '))
# if viruchka > izderzhki:
#     print(f"Прибыль: {viruchka - izderzhki}")
#     print("Рентабельность:", (viruchka - izderzhki)/viruchka)
#     workers = int(input('Сообщите численность сотрудников: '))
#     print("Прибыль на сотрудника:", (viruchka - izderzhki) / workers)
# else:
#     print(f"Убыток: {viruchka - izderzhki}")
# 6.
a = int(input('Сообщите результат в первый день: '))
b = int(input('Сообщите количество километров: '))
i = 1
while a < b:
    i = i + 1
    a = a + a*0.1
print(i)
