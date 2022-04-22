

-------------------------------Задание_1---------------------------------------------------------------
from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Salary - {time * rate + bonus}')
    except ValueError:
        print('Enter all 3 numbers. Not string or empty character.')


salary()

--------------------------------Задание_2--------------------------------------------------------------

original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ansver_list = [el for num, el in enumerate(original_list) if original_list[num - 1] < original_list[num]]
print(original_list)
print(ansver_list)

---------------------------------Задание_3---------------------------------------------------------------------

print(f'Numbers from 20 to 240 are multiples of 20 or 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

---------------вариант решения----------------------------------------------

uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(uniq_list)

----------------------------------Задание_4-----------------------------------------------------------

my_list = [2, 2, 2, 7, 23, 1, 44, 3, 2, 10, 7, 4, 11]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)

---------------вариант решения----------------------------------------------

from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_list = [el for el in my_list if my_list.count(el) == 1]
print(uniq_list)

----------------------------------Задание_5-----------------------------------------------------------

from functools import reduce

def my_func(el_1, el_2):
    return el_1 * el_2

print(f'List of even values {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Result of multiplying all the elements of the list {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

----------------------------------Задание_6-----------------------------------------------------------

from itertools import cycle, count

v_start = int(input('Start number: '))
v_stop = v_start * 2 + 10 + 1

# v.1
for i in count(v_start):
    if i < v_stop:
        print(i)
    else:
        break
del i

# v.2
my_list = [i for i in range(v_stop)]
count = 0
for b in cycle(my_list):
    if count < v_stop + 10:
        print(b)
        count += 1
    else:
        break

----------------------------------Задание_7-----------------------------------------------------------

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break



