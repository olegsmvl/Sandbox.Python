import re
import operator

def learned(filename):
    with open(filename, 'r') as file:
        word_set = set()
        
        # Читаем файл построчно
        for line in file:        
                    # Разделяем строку на слова
            words = line.split()
            
            # Добавляем каждое слово в множество
            for word in words:
                word_set.add(word)

    return word_set

def exclude_words():
    learned_words = learned('learned/learned.txt')
    print(f'my dictionary count: {len(learned_words)}')
    names = learned('learned/names.txt')
    learning_words = learned('learned/learning_words.txt')
    learning_gramma = learned('learned/learning_gramma.txt')
    exclude = learned_words.union(names).union(learning_words).union(learning_gramma)
    return exclude


frequency = {}
#########################
film_name = 'a_scanner_darkly.txt'
#########################
document_text = open(film_name, 'r')
text_string = document_text.read().lower()
exclude = exclude_words()

match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
already_known_words = {}
for word in match_pattern:
    if not word in exclude:
        count = frequency.get(word,0)
        frequency[word] = count + 1
    else:
        count = already_known_words.get(word,0)
        already_known_words[word] = count + 1
    
frequency_sorted = dict(sorted(frequency.items(), key=operator.itemgetter(1), reverse=True))

frequency_list = frequency_sorted.keys()

frequency_out_file = 'out.txt'
f = open(frequency_out_file, 'w')

for words in frequency_list:
    first = words
    second = frequency_sorted[words]
    f.write(f'{first} \t{second} \n')
    #print (words, frequency_sorted[words])

print(f'already known words: {len(already_known_words)}')
print(f'new words count: {len(frequency_list)}')
f.close()