import re, os, sys
from os import listdir
from os.path import isfile, join

def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def getMonth(m, y) :
    if m == "january": return 31
    if m == "february": 
        if isLeapYear(y):
            return 29
        return 28
    if m == "march": return 31
    if m == "april": return 30
    if m == "may": return 31
    if m == "june": return 30
    if m == "july": return 31
    if m == "august": return 31
    if m == "september": return 30
    if m == "october": return 31
    if m == "november": return 30
    if m == "december": return 31

title = str(sys.argv[1])
print(title)

if re.match("^Solution:", title):
    [year, month, day] = title.split(":")[1].strip().split("/")
    month = month.lower()

    max_days = getMonth(month, int(year))
    path = "./" + year + "/" + month + "/"

    readme = open(path + "readme.md", 'w')
    readme.write("# " + month.capitalize() + " Challenge\n\n## Available Solutions\n")
    readme = open(path + "readme.md", 'a')

    outer_files = os.listdir(path)

    for i in range(1, max_days + 1):
        if ("day-" + str(i)) in outer_files:
            new_path = path + "day-" + str(i)
            files = [file for file in listdir(new_path) if isfile(join(new_path, file))]
            print(files)

            if len(files) > 1:
                readme.write("- [x] Day " + str(i) + " - [Solution](./day-" + str(i) + "/readme.md)\n")
            else:
                readme.write("- [ ] Day " + str(i) + " -\n")
        else:
            readme.write("- [ ] Day " + str(i) + " -\n")    

    readme.close()
