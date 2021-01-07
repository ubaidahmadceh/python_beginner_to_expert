file_opener = open('file.txt', 'r')

file_reader = file_opener.read()

print(file_reader.count("india"))

file_opener.close()