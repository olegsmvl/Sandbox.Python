import json
import re
import operator

# Открываем файл JSON для чтения
with open('in_text.json', 'r') as file:
    chat = json.load(file)

data = chat["messages"]
    
    # Проверяем, является ли data списком
if isinstance(data, list):
    # Вывод количества элементов в списке
    print(f"Число элементов в списке: {len(data)}")
else:
    print("Данные не являются списком")

count_msgs = 0

person = ""

with open('/home/fly/temp/settings_chat.ini', 'r') as file:
    person = file.readline().strip()

all_text = ""

for msg in data:
    if msg["type"] == "message" and msg["from"] == person:
        count_msgs += 1
        text = msg["text"]
        if not isinstance(text, list):
            all_text += text

match_pattern = re.findall(r'\b[а-я]{3,15}\b', all_text)

frequency = {}

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_sorted = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))

frequency_list = frequency_sorted.keys()

frequency_out_file = 'out.txt'
f = open(frequency_out_file, 'w')

for words in frequency_list:
    first = words
    second = frequency_sorted[words]
    f.write(f'{first} \t{second} \n')

# print(all_text)