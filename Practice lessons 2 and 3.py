# ЗАНЯТИЕ 2

from typing import List

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import warnings

warnings.filterwarnings('ignore')

# Задание 1

x = np.linspace(0, 10, 11)

sum_qrt = 0
for i in range(len(x)):
    sum_qrt = sum_qrt + x[i]**2
len_x = np.sqrt(sum_qrt)
print("Задание 1 - ", (len_x))

# Задание 3.1

x = []
x2 = []
y = []
y2 = []

for i in range(1500):
    r = 1000
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(r ** 2 - i ** 2))
    y2.append(-np.sqrt(r ** 2 - i ** 2))

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='g')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='y')
plt.plot(x2, y, color='b')
plt.axis('scaled')
print("Окружность")
plt.show()


# Задание 3.2

x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 40
    b = 20
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 - (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='g')
plt.plot(x, y2, color='r')
plt.plot(x2, y2, color='y')
plt.plot(x2, y, color='b')
plt.axis('scaled')
print("Элипс")
plt.show()

# Задание 3.3

x = []
x2 = []
y = []
y2 = []

for i in range(1000):
    a = 400
    b = 200
    x.append(-i)
    x2.append(i)
    y.append(np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))
    y2.append(-np.sqrt(b ** 2 + (b ** 2 * (i ** 2 / a ** 2))))

plt.plot(x, y, color='r')
plt.plot(x, y2, color='b')
plt.plot(x2, y2, color='b')
plt.plot(x2, y, color='r')
plt.axis('scaled')
print("Гиперболы")
plt.show()

# Задание 5.1

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = 10*X + 2*Y
Z1 = 10*X + 2*Y + 100
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z1)
print("Трехмерный график двух параллельных плоскостей")
show()

# Задание 5.2

fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2
ax.plot_surface(X, Y, Z)
ax.plot_surface(X, Y, Z + 50)
print("Трехмерный график двух поверхностей второго порядка")
show()

# ЗАНЯТИЕ 3

# Задание 1

x = np.linspace(-2*np.pi, 3*np.pi, 201)

k, a, b = np.linspace(2, 10, num = 3)
k1, a1, b1 = np.linspace(11, 20, num = 3)
k2, a2, b2 = np.linspace(21, 30, num = 3)

plt.figure(figsize = (10, 5))
plt.plot(x, k * np.cos(x - a) + b, label='k, a, b')
plt.plot(x, k1 * np.cos(x - a1) + b1, color='g', label='k1, a1, b1')
plt.plot(x, k2 * np.cos(x - a2) + b2, color='r', label='k2, a2, b2')

plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(frameon=False)
print("график функции: y(x) = k∙cos(x – a) + b")
plt.show()

# Задание 3.1

r = int(input("Введите значение полярного радиуса - "))
a = int(input("Введите значение полярного угла - "))
if r >= 0 and 2*np.pi >= a >= 0:
    x = r*np.cos(a)
    y = r*np.sin(a)
    print("Полярные координаты в декартовы")
    print('X =', x)
    print('Y =', y)
else:
    print('Параметры не соответствуют области определения')

# Задание 3.2

phi = np.arange(0., 2., 1./180.)*np.pi
plt.polar(phi, [10]*len(phi))
print('График окружности в полярных координатах')
plt.show()

# Задание 3.3

r = int(input("Введите значение полярного радиуса - "))
a = int(input("Введите значение полярного угла - "))
a = 0.3*np.pi
x = r*np.cos(np.linspace(0, r, 1000))
y = 3*x + 1
plt.polar(x, y)
print('График отрезка прямой линии в полярных координатах')
plt.show()

# Задание 4

x = np.linspace(-2, 3, 201)
plt.figure(figsize=(6, 12))
plt.plot(x, (- 1 / x) + 2)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)
print("График системы")
plt.show()
from scipy.optimize import fsolve
def equations(p):
    x, y = p
    return (x ** 2 - 1 - y, (- 1 / x) + 2 - y)
x1, y1 = fsolve(equations, (2, 4))
x2, y2 = fsolve(equations, (0.5, 0.5))
x3, y3 = fsolve(equations, (-1, 1))
print("Решение системы уравнений и неравенств:")
print(x1, y1)
print(x2, y2)
print(x3, y3)