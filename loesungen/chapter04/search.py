from os import listdir
from os.path import isfile
from sys import argv, exit

def consider(filename):
    extensions = ['txt', 'html', 'xml', 'md', 'csv', 'py']
    for extension in extensions:
        if filename.endswith(f'.{extension}'):
            return True
    return False

if __name__ == '__main__':
    if len(argv) < 3:
        print(f"Usage: python3 {argv[0]} DIRECTORY STRING")
        exit()
    directory = argv[1]
    string = argv[2]
    for filename in listdir(directory):
        path = argv[1] + '/' + filename
        if isfile(path) and consider(filename):
            with open(path, 'r') as f:
                text = f.read()
                if string in text:
                    print(filename)
