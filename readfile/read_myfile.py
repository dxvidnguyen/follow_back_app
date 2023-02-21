import os

pathway = os.path.join(os.getcwd(), "myfile.txt")
f = open(pathway)
content = f.readlines()

mystr = ""

for line in content:
   mystr += ''.join(line.splitlines()) + ' '

print(mystr)




