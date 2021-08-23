from os import listdir
from os.path import isfile, isdir
from sys import argv

def print_dir(directory, indent = 0):
    for entry in listdir(directory):
        path = f"{directory}/{entry}"
        if isdir(path):
            prefix = 'D'
        elif isfile(path):
            prefix = 'F'
        else:
            prefix = '?'
        print(f"{' ' * indent}{prefix} {entry}")
        if isdir(path):
            print_dir(path, indent + 4)

if __name__ == '__main__':
    if len(argv) > 1:
        directory = argv[1]
    else:
        directory = '.'
    print_dir(directory)
