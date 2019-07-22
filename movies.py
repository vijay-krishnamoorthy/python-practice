import csv
path="C:\\Users\\Admin\\Desktop\\python-vijay\\movies.csv"


lines=[line for line in open(path)]
for line in lines:
    l=list(line.strip().split(','))
    print(l)

file = open(path, newline='')
reader = csv.reader(file)
header=next(reader)
data =[row for row in reader]

for i in data:
    print(i)