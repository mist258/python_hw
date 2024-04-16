import math
from itertools import groupby
# strings
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

str1 = 'as 23 fdfdg544'
str2 = ''
for ch in str1:
    if ch.isdigit():
        str2 += ch
print(','.join(str2))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'
st2 = []
for ch in st:
    ch.split()
    if ch.isalpha():
        continue
    else:
        st2.append(ch)
print(''.join(st2).replace(' ', ', ').lstrip(','))

# list comprehension
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'
greet = [ch1.upper() for ch1 in greeting]
print(greet)
# 2) з діапазону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
x1 = [i**2 for i in range(50) if i %2 !=0]
print(x1)

# function
# - створити функцію яка виводить ліст


def funct(n):
    l = []
    for i in range(n+1):
        l.append(i)
    print(l)


funct(10)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def num(a, b, c):
    largest = a
    if c >= largest:
         largest = c
    if b >= largest:
         largest = b
    else:
        largest = a
    print(largest)


num(1100, 407, 1100)
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше


def numbers(*args):
    list_num = []
    for num in args:
        list_num.append(num)
    print(str(max(list_num)))
    print(str(min(list_num)))
    return str(min(list_num))


numbers(45,-7,365,-56,25)

# - створити функцію яка повертає найбільше число з ліста


def max_num(some_lst):
    numb = (int(input("Enter some numbers:")))
    for n in range(numb):
        elem = int(input("Enter element of list:"))
        lst2.append(elem)
    print(max(some_lst))
    return max(some_lst)


lst2 = []
max_num(lst2)

# - створити функцію яка повертає найменьше число з ліста


def min_num(some_lst1):
    numb = (int(input("Enter some numbers:")))
    for n in range(numb):
        elem = int(input("Enter element of list:"))
        lst3.append(elem)
    print(min(some_lst1))
    return min(some_lst1)


lst3 = []
min_num(lst3)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.


def multiple_list(some_lst2):
    num1 = int(input("Enter a number:"))
    for n in range(num1):
        num2 = int(input("Enter a number for list:"))
        lst4.append(num2)
    print(math.prod(some_lst2))
    return math.prod(some_lst2)


lst4 = []
multiple_list(lst4)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.


def sum_list(some_list3):
    num = (int(input("Enter a number: ")))
    for n in range(num):
        num_l = int(input('Enter a number for list: '))
        lst5.append(num_l)
    print(sum(some_list3) // len(some_list3))


lst5 = []
sum_list(lst5)


# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число

list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
list_minimum = min(list)
print(list_minimum)

#   - видалити усі дублікати

list_d = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
list_sort = sorted(list_d)
list_origin = [i for i, _ in groupby(list_sort)]
print(list_origin)

#   - замінити кожне 4-те значення на 'X'

list_c = [22, 3,5,2,8,2,-23, 8,23,5]
for i in range(3,len(list_c), 4):
    list_c[i] = 'X'
print(list_c)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

n = 6
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# 3) вывести табличку множення за допомогою цикла while
rows = 10
columns = 10
row = 1

while row <= rows:
    column = 1
    while column <= columns:
        res = row * column
        print(f"{res:3}", end=" ")
        column += 1
    print()
    row += 1

# 4) переробити це завдання під меню

while True:
    print('1  find min digit')
    print('2  delete all duplicates')
    print('3  change every 4-th value')
    print('4  lists average value')
    print('5  exit')

    entry = input('Enter your choice: ')

    if entry == '1':
        print(list_minimum)
    elif entry == '2':
        print(list_origin)
    elif entry == '3':
        print(list_c)
    elif entry == '4':
        sum_list(lst5)
    else: break
