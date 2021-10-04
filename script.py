import os, sys, calendar, requests, json
from calendar import monthrange

token = os.environ['TOKEN']
issue_number = int(sys.argv[1])
header = {'Authorization': 'token ' + token, 'Accept': 'application/vnd.github.v3+json'}
url = "https://api.github.com/repos/vitspot/leetcode-daily/issues/" + str(issue_number)
response = requests.get(url, headers=header)
body = response.json()["body"]
print(body)

temp = body.split("### Question Name:")[1].split("### Question URL:")
qname = temp[0].strip()
body = temp[1]
temp = body.split("### Leetcode Question:")
qurl = temp[0].strip()
body = temp[1]
temp = body.split("### Date:")
question = temp[0].strip()
body = temp[1]
temp = body.split("### Language:")
date = temp[0].strip()
body = temp[1]
temp = body.split("### Solution:")
lang = temp[0].strip()
soln = temp[1].strip()

[day, month, year] = list(map(int, date.split("/")))
month_num = month
month = calendar.month_name[month].lower()

path = os.getcwd()
# In the root dir

if str(year) not in os.listdir(path):
    os.mkdir(os.path.join(path, str(year)))
    path = os.path.join(path, str(year))
    os.chdir(path)
else:
    path = os.path.join(path, str(year))
    os.chdir(path)
# In the year dir

year_readme = open("readme.md", "w")
year_readme.write("# " + str(year) + "\n\n## Submissions")
year_readme.close()

if month not in os.listdir(path):
    os.mkdir(os.path.join(path, month))
    path = os.path.join(path, month)
    os.chdir(path)
else:
    path = os.path.join(path, month)
    os.chdir(month)
# In the month dir

if "readme.md" not in os.listdir(path):
    month_readme = open("readme.md", "w")
    lines_list = []
    lines_list.append("# " + month.capitalize() + " Challenge\n")
    lines_list.append("\n")
    lines_list.append("## Available Solutions\n")
    for i in range(1, monthrange(year, month_num)[1] + 1):
        lines_list.append("- [ ] Day " + str(i) + " -\n")
    month_readme.writelines(lines_list)    
    month_readme.close()

if ("day-" + str(day)) not in os.listdir(path):
    os.mkdir(os.path.join(path, "day-" + str(day)))
    path = os.path.join(path, "day-" + str(day))
    os.chdir(path)
else:
    path = os.path.join(path, "day-" + str(day))
    os.chdir(path)
# In the day dir

if "readme.md" not in os.listdir(path):
    day_readme = open("readme.md", "w")
    if question != "":
        day_readme.write("## Question:\n\n" + question + "\n\n## Solutions:")
    else:
        day_readme.write("## Question:\n\n" + qname + "\n\n## Solutions:")    
else:
    day_readme = open("readme.md", 'r')
    data = day_readme.read().split("## Solutions")[0].strip()
    day_readme = open("readme.md", 'w')
    day_readme.write(data + "\n\n## Solutions:")
# Added initial question data

files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
soln_num = len(files)
new_soln = open("solution" + str(soln_num) + "." + lang.lower(), "w")
new_soln.write(soln)
new_soln.close()
# Added new solution

j = 1
files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
files.sort()

for i in files:
    if i != "readme.md":
        ext = i.split('.')[1].capitalize()
        day_readme.write("\n" + str(j) + ". [Submission " + str(j) + "](./" + i + ") (" + ext + ")")
        j += 1
day_readme.close()
# Made day README

def getBadges(path, lang, ext, slug, day, color):
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and file.endswith(ext)]
    files.sort()
    badge = "![" + lang + "](https://img.shields.io/badge/" + lang + "-" + str(len(files)) + "-" + color + "?style=social&logo=" + slug + ") "
    solution = badge + " "
    for i in range(0, len(files)):
        solution += ("[" + str(i + 1) + "](./day-" + day + "/" + files[i] + ") ")
    if len(files) > 0:
        return solution
    else:
        return ""

os.chdir("../")
path = os.getcwd()

month_readme = open("readme.md", "r")
lines_list = month_readme.readlines()
dirs = os.listdir(path)
if ("day-" + str(day)) in dirs and len(os.listdir(os.path.join(path, "day-" + str(day)))) > 1:
    cpp = getBadges(os.path.join(path, "day-" + str(day)), "C++", ".cpp", "cplusplus", str(day), "blue")
    java = getBadges(os.path.join(path, "day-" + str(day)), "Java", ".java", "java", str(day), "red")
    py = getBadges(os.path.join(path, "day-" + str(day)), "Python", ".py", "python", str(day), "yellow")
    lines_list[day + 2] = "- [x] Day " + str(day) + "- [" + qname + "](" + qurl + ") - [Solutions](./day-" + str(day) + "/readme.md) " + cpp + java + py + "\n"
    month_readme = open("readme.md", "w")
    month_readme.writelines(lines_list)
month_readme.close()    

os.chdir("../")
path = os.getcwd()

year_readme = open("readme.md", "a")

for i in range(1, 13):
    dirs = os.listdir(path)
    if calendar.month_name[i].lower() in dirs:
        year_readme.write("\n- [" + calendar.month_name[i] + "](./" + calendar.month_name[i].lower() + "/readme.md)")
year_readme.close()
# Made year README
