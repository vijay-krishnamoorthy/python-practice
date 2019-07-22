import csv
import datetime
import re
path = "C:\\Users\\Admin\\Desktop\\python-vijay\\google-stock.csv"
return_path = "C:\\Users\\Admin\\Desktop\\python-vijay\\after-stock.csv"
'''
file_read=open(path,newline='')
reader=csv.reader(file_read)
header=next(reader)
file_write =open(return_path, 'w')
writer=csv.writer(file_write)
for data in reader:
    i=int(float(data[1]))
    if(i>700):
        writer.writerow(data)
    
file_read.close()
file_write.close()
open_again=open(path,newline='')
read = csv.reader(open_again)
header=next(read)
for i in read:
    print(i)


'''
date_ = '05/07/2017'
# print(datetime.date.strftime(date_,"%dd/%mm/%Y"))
lastconnection = datetime.datetime.strptime("21/12/2008", "%d/%m/%Y").strftime('%d/%m/%Y')
match_obj=re.match(r'[0-9]{2}\/[0-9]{2}\/[0-9]{4}',lastconnection)
print(match_obj.group(0))
print(lastconnection)
