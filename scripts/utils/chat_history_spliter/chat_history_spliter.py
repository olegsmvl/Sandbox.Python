# morph instruction
# https://pymorphy2.readthedocs.io/en/stable/user/guide.html#id2

import json
import re
import operator
import pymorphy2
from translate import Translator

def main():
    # Создание объекта переводчика с указанием целевого языка
    translator = Translator(to_lang="en", from_lang="ru")

    # Перевод текста
    result = translator.translate("оказалось")

    print(result)

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
    morph = pymorphy2.MorphAnalyzer()

    for word in match_pattern:
        if 'VERB' in morph.parse(word)[0].tag:
            word_normal = get_normal(morph, word)
            count = frequency.get(word_normal,0)
            frequency[word_normal] = count + 1

    frequency_sorted = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))

    frequency_list = frequency_sorted.keys()

    frequency_out_file = 'out.txt'
    f = open(frequency_out_file, 'w')

    for words in frequency_list:
        first = words
        second = frequency_sorted[words]
        f.write(f'{first} \t{second} \n')

def get_normal(morph, word):
    p = morph.parse(word)[0]
    return p.normalized.normal_form

def get_part_of_speech(morph, word):
    p = morph.parse(word)[0]
    return p.normalized.normal_form

main()

# print(all_text)