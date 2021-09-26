import re, os, sys
from os import listdir
from os.path import isfile, join

def getMonth(m):
    if m == 1: return "january"
    if m == 2: return "february"
    if m == 3: return "march"
    if m == 4: return "april"
    if m == 5: return "may"
    if m == 6: return "june"
    if m == 7: return "july"
    if m == 8: return "august"
    if m == 9: return "september"
    if m == 10: return "october"
    if m == 11: return "november"
    if m == 12: return "december"

title = str(sys.argv[1])
print(title)

if re.match("^Solution: ([0-9]{1}|[0-9]{2})/([0-9]{1}|[0-9]{2})/[0-9]{4}$", title):
    [day, month, year] = list(map(int, title.split(":")[1].split("/")))

    month = getMonth(month)
    path = "./" + str(year) + "/" + str(month) + "/day-" + str(day) + "/"

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
