# 1.
# my_list = []
# with open('1.txt', 'w') as f:
#     while True:
#       stroka = input("Введите строку: ")
#       if not stroka:
#           break
#       my_list.append(stroka+'\n')
#     f.writelines(my_list)

# # 2.
# my_list = []
# with open('1.txt', 'r', encoding = 'utf-8') as f:
#     my_list = f.readlines()
# print("Всего строк в файле: ", len(my_list))
# j = 0
# quantity = 0
# for i in my_list:
#     j += 1
#     new_list = i.split(' ')
#     x = new_list.count('')
#     quantity = len(new_list) - x
#     print(f"В {j}й  строке: {quantity} слова")

# 3.
# average = 0
# with open('1.txt', 'r', encoding = 'utf-8' ) as f:
#     my_str = f.read()
#     my_str = my_str.replace('\n',' ')
#     new_list = my_str.split(' ')
#     for i in range(0, len(new_list), 2):
#         if float(new_list[i+1]) < 20000:
#             print(new_list[i])
#         average += float(new_list[i+1])
#     print("Средний доход: ", average/(len(new_list)/2) )

# 4.
# with open('2.txt', 'w', encoding='utf-8') as new_f:
#     pass
# with open('1.txt', 'r', encoding = 'utf-8' ) as f:
#     for line in f:
#         line = line.split(" ")
#         if line[0] == 'One':
#             line[0] = 'Один'
#         elif line[0] == 'Two':
#             line[0] = 'Два'
#         elif line[0] == 'Three':
#             line[0] = 'Три'
#         elif line[0] == 'Four':
#             line[0] = 'Четыре'
#         str_line = ''.join(line)
#         with open('2.txt', 'a', encoding='utf-8') as new_f:
#             new_f.write(str_line)

# 5.
# my_list = []
# with open('1.txt', 'w', encoding = 'utf-8') as f:
#     while True:
#       stroka = input("Введите числа: ")
#       if not stroka:
#           break
#       my_list.append(stroka+'\n')
#     f.writelines(my_list)
# with open('1.txt', 'r', encoding = 'utf-8') as f:
#     my_list = f.readlines()
# summa = 0
# for i in my_list:
#     i = i.replace('\n','')
#     new_list = i.split(' ')
#     for j in range(len(new_list)):
#         try:
#             summa += float(new_list[j])
#         except Exception:
#             pass
# print('Сумма чисел: ', summa)

# 6.
# import re
# with open('1.txt', 'r', encoding = 'utf-8') as f:
#     my_list = f.readlines()
# regex_num = re.compile('\d+')
# regex_predm = re.compile('[а-яА-ЯёЁ]+')
# my_dictionary = {}
# for i in my_list:
#     digit = regex_num.findall(i)
#     my_sum =0
#     for j in range(len(digit)):
#         my_sum += int(digit[j])
#     predm = regex_predm.search(i).group()
#     my_dictionary.update({predm :my_sum})
# print(my_dictionary)

# 7.
# import re
# import json
# with open('1.txt', 'r', encoding = 'utf-8') as f:
#     my_list = f.readlines()
# regex_num = re.compile('\d+')
# my_dictionary = {}
# my_sum = 0
# j = 0
# average_profit = 0
# for i in my_list:
#     firm = i.split(' ')
#     digit = regex_num.findall(' '.join(firm[1:]))
#     profit = int(digit[0]) - int(digit[1])
#     my_dictionary.update({firm[0]: profit})
#     if profit > 0:
#         my_sum += profit
#         j += 1
#         if j == 0:
#             average_profit = 0
#         else:
#             average_profit = my_sum/j
# my_list = [ my_dictionary, {"average_profit": average_profit}]
# print(my_list)
# with open("my_file.json", "w") as write_f:
#     json.dump(my_list, write_f)



