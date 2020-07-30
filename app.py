from sys import argv

file_name = ''
finded_import_objects=set()

if len(argv) > 1:
    file_name = argv[1]
    

with open(file_name) as f:
    for line in f:
        if 'import ' in line:
            import_objects = ''.join(line.strip().split('import')[1:]).replace(' ', '')
            finded_import_objects.update(import_objects.split(','))
        else:
            for import_object in finded_import_objects.copy():
                if import_object in line:
                    finded_import_objects.discard(import_object)

print('Imported objects are not used: ', str(finded_import_objects))

