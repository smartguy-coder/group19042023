# with open('files5555.py', mode='w+', encoding='utf-8') as my_file:
#     content = my_file.read()
#     # content = my_file.readlines()
#     print(content)
#     my_file.write('print(555)\n')


# with open('files.py', mode='r+', encoding='utf-8') as my_file:
#     content = my_file.readlines()
#     for line in content:
#         print(line, end='')

# with open('new.txt', mode='a', encoding='utf-8') as my_file:
#     letters = my_file.write('1\n')
#     print(letters)

# with open('data.csv', mode='r', encoding='utf-8') as my_file:
#
#     with open('new_data.csv', mode='a+', encoding='utf-8') as new_file:
#
#         content = my_file.readlines()
#         for line in content[1:]:
#             product = line.strip().split(';')
#             product_cost = float(product[1].replace(',', '.')) * float(product[2].replace(',', '.'))
#             print(product_cost)
#             new_file.write(f'{product[0]}|||{product_cost}' + '\n')

import csv

# with open('data2.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)
#
# row = ['David', 30, 183]
# row2 = ['John', 33, 170]

# with open('data3.csv', mode='a', encoding='utf-8') as file:
#     writer = csv.writer(file)
#
#     writer.writerow(row)
#     writer.writerow(row2)

# with open('data2.csv', mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file, fieldnames=['product', 'code', 'remains'], delimiter=';')
#     print(reader)
#     for row in list(reader)[1:]:
#         print(row)

# import requests
#
# url = 'https://gdb.rferl.org/4db364a8-b56b-46e0-9c11-193860bec549_w1023_r1_s.jpg'
# url2 = 'https://nazk.gov.ua/wp-content/uploads/2021/02/Zvit-pro-finansovi-rezultaty-za-2020-rik-forma-2-ds.pdf'
#
# responce = requests.get(url2)
# print(responce.content)
#
# with open(file='wiosna_kwitnace_drzewa_1170.jpg', mode='rb') as picture_file:
#     spring = picture_file.read()
#     print(spring)
#
#     with open(file='spring.jpg', mode='wb') as target_file:
#         target_file.write(spring)


# with open('data2.csv', mode='r', encoding='utf-8') as source:
#     content = source.readlines()
#
#     start = 1
#     for line in content:
#         with open(fr'folder\{start}.txt', mode='w', encoding='utf-8') as temp_file:
#             temp_file.write(line)
#         start += 1
