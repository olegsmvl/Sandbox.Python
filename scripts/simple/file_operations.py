import os

def create_file(file_name):
    f = open(file_name, 'w')
    f.write('create text')
    f.close()

def read_file(file_name):
    f = open(file_name, 'r')
    print(f.read())
    f.close()

def update_file(file_name):
    f = open(file_name, 'a')
    f.write('\n')
    f.write('new line')
    f.close()

def remove_file(file_name):
    os.remove(file_name)

def replace_text(file_name, old_word, new_word):
    f = open(file_name, 'r')
    text = f.read()
    f.close()

    text = text.replace(old_word, new_word)

    with open(file_name, 'w') as file:
        file.write(text)

def main():
    file_name = 'file.txt'
    create_file(file_name)
    update_file(file_name)
    replace_text(file_name, 'line', 'block_buster')
    read_file(file_name)
    #remove_file(file_name)

main()