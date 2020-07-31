from sys import argv
from save_import import save_import
from delete_import import delete_import

file_name = ''
finded_import_objects=set()

if len(argv) > 1:
    file_name = argv[1]
    

with open(file_name) as f:
    for line in f:
        if 'import ' in line:
            save_import(line, finded_import_objects)
        else:
            delete_import(line, finded_import_objects)

print('Imported objects are not used: ', str(finded_import_objects))

