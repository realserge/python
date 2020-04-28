#1.
result_list = [2, 'text', 456, 45.3, None]
for el in result_list:
    print(type(el))
#2.
list = input("Введите список ").split()
j = 0
for i in range(int(len(list) / 2)):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2

print(list)
#3.
winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
month = int(input('Choose a month: '))
if month in winter:
    print("winter")
if month in spring:
    print("spring")
if month in summer:
    print("summer")
if month in autumn:
    print("autumn")

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}
month = int(input('Choose a month: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
#4.
i = 0
for word in input("Введите строку из нескольких слов, разделённых пробелами ").split():
    i+=1
    print(i," ",word[:10])
#5.
my_list = [7, 5, 3, 3, 2]
value=int(input("Введите число "))
max_value = max(my_list)
if value > max_value:
        my_list.insert(0,value)
elif value in my_list:
        my_list.insert(my_list.index(value),value)
else:
        my_list.append(value)

print(my_list)

#6.
mydict={}
mycort=()
megaresult = {}
result_list = []
i=0
list1= []
list2 = []
list3 = []
list4 = []
while i < 3:
    i+=1
    mydict['название']=str(input("название "))
    mydict['цена']=str(input("цена "))
    mydict['количество']=str(input("количество "))
    mydict['ед']=str(input("ед "))
    mycort=(i,mydict)
    result_list.append(mycort)



print(result_list)