 #!/usr/bin/env python3

import os, sys

rootdir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    
handlers = {}

handlers[".*python.*"] = "docs/it/python"
handlers[".*(js)|(JavaScript).*"] = "docs/it/js"

for subdir, dirs, files in os.walk(rootdir):
    #Обробляємо тільки перший рівень каталогу
    if subdir != rootdir:
        break
    print("Currect directory: {}".format(subdir))
    print("\nDirectories:")
    for dir in dirs:
        print("  " + dir)
        for mask, destination in handlers.items():
            #ВИПРАВИТИ: якщо дір відповідає по регексу маск
            if dir == mask:
                #обробити dir
                break
    print("\nFiles:")
    for file in files:
        #print("  " + os.path.join(subdir, file))
        for mask, destination in handlers.items():
            #ВИПРАВИТИ: якщо file відповідає по регексу маск
            if file == mask:
                #обробити file
                break
        print("  " + file)