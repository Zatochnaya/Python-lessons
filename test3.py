#Задание 1

def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero forbidden!!!"
    return round(div_num, 4)

print(div(input("Enter first number - "), input("Enter second - ")))

#Задание 2

def personal_info(**kwargs):
    return ' '.join(kwargs.values())

print(personal_info(name=input("Enter your name: "), surname=input("Enter your surname: "),
                    birthday=input("Enter your birthday: "), city=input("Enter your city: "),
                    email=input("Enter your email: "), phone_number=input("Enter your phone number: ")))

#Задание 3

def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Enter only a numbers!"

print(my_func(2, 11, -30))

#Задание 4

def my_pow_fun(x, y):
    try:
        res = x ** y
    except TimeoutError:
        return "Enter a float number and a negative power"
    return res

print(my_pow_fun(4.5, -2))

#Задание 4 вариант 2

def my_func2(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не выполнено условие ввода данных:\nx должен быть быльше 0\ny должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения х в степень y = {round(result, 6)}'
    except ValueError:
        return "Программа работает только с числами."

number1 = input('Введите действительное положительное число, х = ')
number2 = input('Введите целое отрицательное число, y = ')

print(my_func2(number1, number2))


#Задание 5


def sum_num():
    s = 0
    while True:
        in_list = input("Enter a number, input 'q' to exit ").split()
        for num in in_list:
            if num.lower() == "q":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print("To exit the program, enter - 'q'.")
        print(f"Sum of numbers = {s}")


print(sum_num())


#Задание 6 и 7


def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Введите строку из слов разделённых пробелом: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(result, ' ')