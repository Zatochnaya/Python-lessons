import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, +5, 200)
y = np.cos(x)

fig, ax = plt.subplots()

line1, = ax.plot(x, y,label='Точки(X)')
line1.set_dashes([2, 0.5])
line2, = ax.plot(x, y - 7, dashes=[20, 5], label='Пунктир(Y)')

ax.legend()
plt.show()