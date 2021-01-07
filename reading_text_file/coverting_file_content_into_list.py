file_opener = open('file.txt', 'r') 

read_line_by_line = file_opener.readlines()

countries_list = []

for line in read_line_by_line:
    countries_list.append(line.strip())

print(countries_list)
