# create a file

file = open("file.txt", 'r')

for i in file.readline():
    print(i, end="")

file.close()

