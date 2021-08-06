try:
    file = open("test.txt", "r")
    for i in file:
        print(i, end='')
except FileExistsError as e:
    print(e)
finally:
    if file.name == 'test.txt':
        print("File already exists")
    else:
        print("there is no test.txt file, so we are created this file")
        file = open("test.txt", "w")
