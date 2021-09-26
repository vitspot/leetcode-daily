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
    if m == 1: return ["january", 31]
    if m == 2: 
        if isLeapYear(y):
            return ["february", 29]
        return ["february", 28]
    if m == 3: return ["march", 31]
    if m == 4: return ["april", 30]
    if m == 5: return ["may", 31]
    if m == 6: return ["june", 30]
    if m == 7: return ["july", 31]
    if m == 8: return ["august", 31]
    if m == 9: return ["september", 30]
    if m == 10: return ["october", 31]
    if m == 11: return ["november", 30]
    if m == 12: return ["december", 31]

title = str(sys.argv[1])
print(title)

if re.match("^Solution: ([0-9]{1}|[0-9]{2})/([0-9]{1}|[0-9]{2})/[0-9]{4}$", title):
    [day, month, year] = list(map(int, title.split(":")[1].split("/")))

    [month, max_days] = getMonth(month, year)
    path = "./" + str(year) + "/" + str(month) + "/"

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
