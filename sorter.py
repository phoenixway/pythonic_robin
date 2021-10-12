 #!/usr/bin/env python3

import os, sys

# class TypeHandler:
#     def __init__(self, filename_mask, destination_folder) -> None:
#         self.filename_mask = filename_mask
#         self.drestination_folder = destination_folder
#     def check(name):
#         return False
#     def process(name):
#         pass


rootdir = os.getcwd()
if len(sys.argv) > 1:
    rootdir = sys.argv[1]

handlers = {}

handlers[".*python.*"] = "docs/it/python"
handlers[".*(js)|(JavaScript).*"] = "docs/it/js"

for subdir, dirs, files in os.walk(rootdir):
    #Обробляємо тільки перший рівень каталогу
    if subdir != rootdir:
        break
    print("Currect directory: {}".format(subdir))
    print("Directories:")
    for dir in dirs:
        print("  " + dir)
        for mask, destination in handlers.items:
            #ВИПРАВИТИ: якщо дір відповідає по регексу маск
            if dir == mask:
                #обробити dir
                break
    print("Files:")
    for file in files:
        #print("  " + os.path.join(subdir, file))
        for mask, destination in handlers.items:
            #ВИПРАВИТИ: якщо file відповідає по регексу маск
            if file == mask:
                #обробити file
                break
        print("  " + file)