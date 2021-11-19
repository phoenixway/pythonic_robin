 #!/usr/bin/env python3
import random, os

def getQuote():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    #print(current_dir)
    filename = current_dir+"/"+'quotes.txt'
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    n = random.randint(0,len(lines)-1)
    return lines[n]