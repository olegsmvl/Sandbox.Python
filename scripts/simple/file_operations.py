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

def main():
    file_name = 'file.txt'
    create_file(file_name)
    update_file(file_name)
    read_file(file_name)
    #remove_file(file_name)

main()