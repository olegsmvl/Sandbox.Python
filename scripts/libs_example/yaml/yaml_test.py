from yaml import dump

# Создаем словарь с данными, которые хотим записать в YAML файл
data = {
    'city': 'New York',
    'name': 'John Doe',
    'age': 30
}

l = []
l.append(data.copy())
l.append(data.copy())

# Открываем файл для записи в режиме 'w' (write)
with open('data.yaml', 'w') as yaml_file:
    # Используем функцию dump из библиотеки PyYAML для записи данных в файл
    dump(l, yaml_file, default_flow_style=False, sort_keys=False)

print("YAML файл успешно создан.")