import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры
d = 16  # размерность вектора PE
positions = np.arange(0, 50)  # позиции
PE = np.zeros((len(positions), d))

# Генерируем каждое измерение
for i in range(d):
    freq = 1 / (10000**(2*i/d))
    if i % 2 == 0:
        PE[:, i] = np.sin(positions * freq)
    else:
        PE[:, i] = np.cos(positions * freq)

# Настройка графика
fig, ax = plt.subplots()
line, = ax.plot([], [], color='red')
ax.set_xlim(0, positions[-1])
ax.set_ylim(-d, d)
ax.set_xlabel('позиция')
ax.set_ylabel('сумма PE')
ax.set_title('Построение суммы позиционного кодирования')
ax.grid(True)

# Функция обновления для анимации
def update(frame):
    signal = PE[:, :frame+1].sum(axis=1)
    line.set_data(positions, signal)
    return line,

# Создаём анимацию
ani = FuncAnimation(fig, update, frames=d, blit=True, interval=500)

ani.save("pe_animation.gif", writer="pillow", fps=2)
