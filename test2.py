# Задание 1

list_of_types = [('!'), (8 + 32), {"плохой пароль": 123312}, ('арбуз'.encode('utf-8')),
                 (43, 421, 6.6), True, [65, 88], (bytes([4, 3, 34, 47])), (4/7),
                 TypeError(404), range(12), None]

for i, item in enumerate(list_of_types, 1):
    print(f"{i}) {item} - {type(item)}")

# Задание 2

list1 = list(input("Введите чётное количество цифр без пробела - "))

for i in range(1, len(list1), 2):
        list1[i-1], list1[i] = list1[i], list1[i - 1]

print(list1)

# Задание 3

n = int(input("Введите число от 1 до 12 - "))

n_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
          8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

n_list = {'зимний': [12, 1, 2], 'весенний': [3, 4, 5], 'летний': [6, 7, 8], 'осенний': [9, 10, 11]}

if n not in n_dict:
    print("Введено некорректное значение, попробуйте снова")
    print(int(input("Введите число от 1 до 12 - ")))
if n in n_dict and n in sum(n_list.values(), []):
    for i in n_list.items():
        if n in i[1]:
            print(f"Вы загадали {i[0]} месяц - {n_dict[n]}")


 # Задание 4


my_string = input('Введите несколько слов, разделённых пробелами - ').split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')



 # Задание 5


my_list = [9, 8, 7, 7, 7, 6, 5, 3, 3, 3, 2, 1]
new_number = ""

while new_number != "q":
    i = 0
    new_number = input("Enter a new rating element in the form of a natural number.\nTo exit - q\n")

    if new_number.isdigit():
        for n in my_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_number))
    print(my_list)


 # Задание 6


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Для каждого выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')
        f_copy[f] = int(pro) if f in 'цена количества' and pro.isdigit() else pro
        analytics[f].append(f_copy[f])
    goods.append((num, f_copy))
    print(f"\nСтруктура товара\n{goods}")
    print(f'\n Текущая аналитика по товарам: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
    print("*" * 30)