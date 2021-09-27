import re, os, sys
from os import listdir
from os.path import isfile, join

title = str(sys.argv[1])
print(title)

if re.match("^Solution:", title):
    [year, month, day] = title.split(":")[1].strip().split("/")
    month = month.lower()
    
    path = "./" + year + "/" + month + "/day-" + day + "/"

    files = [file for file in listdir(path) if isfile(join(path, file))]
    print(files)

    readme = open(path + "readme.md", 'r')
    data = readme.read().split("## Solutions")[0]
    readme = open(path+ "readme.md", 'w')
    readme.write(data)
    readme = open(path+ "readme.md", 'a') 
    readme.write("\n ## Solutions")

    j = 1
    files.reverse()
    for i in files:
        if i != "readme.md":
            readme.write("\n" + str(j) + ". [Submission " + str(j) + "](./" + i + ")")
            j += 1

            #Alternate snippet to append code with syntax highlighting
            #soln = open(path + i, 'r')
            #ext = i.split('.')[1]
            #code = soln.read()
            #readme.write("\n```" + ext + "\n" + code + "\n```")
            #soln.close()
    readme.close()
