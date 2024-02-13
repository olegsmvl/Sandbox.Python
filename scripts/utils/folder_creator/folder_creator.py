import os

def main():
    # Путь к файлу, содержащему список имен папок
    file_path = "folders.txt"

    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Файл '{file_path}' не существует.")
        exit()

    # Создание папок
    with open(file_path, "r") as file:
        for folder_name in file:
            # Удаление пробельных символов и символов новой строки
            folder_name = folder_name.strip()
            
            # Проверка, существует ли папка уже
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                print(f"Папка '{folder_name}' создана.")
            else:
                print(f"Папка '{folder_name}' уже существует.")

main()