import asyncio


async def fetch_data() -> str:
    print("Начало загрузки данных")
    await asyncio.sleep(2)  # Асинхронное ожидание
    print("Данные загружены")
    return "Данные"


async def main():
    result = await fetch_data()
    print("Результат:", result)


# Запуск цикла событий для выполнения корутин
asyncio.run(main())
