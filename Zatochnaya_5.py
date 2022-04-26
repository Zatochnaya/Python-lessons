---------------------------------------Задание 1----------------------------------

my_file = open('text_1.txt', 'w')
line = input('Enter text \n')
while line:
    my_file.writelines(line)
    line = input('Enter text \n')
    if not line:
        break

my_file.close()
my_file = open("text_1.txt", 'r')
content = my_file.readlines()
print(content)
my_file.close()

-------------------------------------------Задание 2--------------------------------------------

my_list = ['Hello\n', 'Hi\n', 'Hey\n']
with open("text_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("text_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")

    -----------------------------------------------Задание 3------------------------------------------------


with open('sal.txt', 'r') as my_file:
    sal = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')


----------------------------------------------------Задание 4---------------------------------------------

rus_dic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('text_4.txt', 'r') as file_obj:
    #content = file_obj.read().split('\n')
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(rus_dic[i[0]] + '  ' + i[1])
    print(new_file)

with open('text_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

------------------------------------------------------Задание 5 --------------------------------------------------
from random import randint

with open("text.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for _ in range (100)]
    my_file.write(" ".join(map(str, my_list)))

print(f"Sum of elements - {sum(my_list)}")

-------------------------------------------------------Задание 6 -------------------------------------------------

import string

with open("text_6.txt", "r", encoding="utf-8") as file:
    print({string.split(":")[0]: sum([int(s[:s.index("(")]) for s in string.split() if "(" in s]) for s in file})

-------------------------------------------------------Задание 7--------------------------------------------------

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')