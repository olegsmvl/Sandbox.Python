from threading import Timer

def my_function():
    print("Таймер сработал!")

# Установка таймера на 2 секунд до запуска функции
timer = Timer(2, my_function)

timer.start()  # Запуск таймера

# перезапуск таймера (по факту создание нового, т.к. тот же таймер нельзя перезапустить)
timer.cancel()
timer = Timer(2, my_function)
timer.start()
