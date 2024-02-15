import os

def create_file(file_name):
    f = open(file_name, 'w')
    f.write('create text')
    f.close()

def create_file_and_folder(file_name):
    dir = os.path.dirname(file_name)
    if not os.path.exists(dir):
        # Создаем папку, если она не существует
        os.makedirs(dir)

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

    file_name_recursive = 'dir1/dir2/file.txt'
    create_file_and_folder(file_name_recursive)
    file_name_recursive2 = 'dir1/dir2/file2.txt'
    create_file_and_folder(file_name_recursive2)

main()