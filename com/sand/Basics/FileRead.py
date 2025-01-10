with open('C:\\CodingPractice\\Python\\com\\sand\\resources\\acronyms.txt') as file:
    result = file.readlines()
    for line in result:
        print(line)


acronym = 'ML'
definition = 'Machine Language'
with open('C:\\CodingPractice\\Python\\com\\sand\\resources\\acronyms.txt', 'a') as file1:
    file1.write(acronym + definition + '\n')


import os
folder = '/Users/shrdhava2/Downloads/'
entries = os.scandir(folder)

for entry in entries:
    if os.path.isfile(entry):
        print('File:', entry.name)
    elif os.path.isdir(entry):
        print('Dir: ', entry.name)

folder_original = '/Users/shrdhava2/Downloads/'
folder_destination = '/Users/shrdhava2/Downloads/Cleaned Up/'
os.mkdir (folder_destination)
location_original = os.path.join(folder_original, 'new.txt')
location_destination = os.path.join(folder_destination, 'new.txt')
os.rename(location_original, location_destination)