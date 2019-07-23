import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
mydb = client['colors']

#list system databases
print(client.list_database_names())

#check if pesons is in the database list
db = client.list_database_names()

if 'colors' in db:
    print("Colors db exists")
else: print("No such DB exists")

#use persons db 
mydb=client['colors']

#creating collections

mycol=mydb['collection_1']

#listing all collections in the database
col_list = mydb.list_collection_names()
print(col_list) 
if 'person' in col_list:
    print("Collection - person exists")
else: 
    print("No such collection exists")

dict = { 'roll': 36,'name': 'vijay','age': 22}
obj = mycol.insert_one(dict)

print(obj)

stud_list = [
    {'roll_no': 1,'name': "vijay",'age':21},
    {'roll_no': 2,'name': "goutham",'age':21},
    {'roll_no': 3,'name': "karthick",'age':23},
    {'roll_no': 4,'name': "nithil",'age':22},
    {'roll_no': 5,'name': "shyam",'age':25},
    {'roll_no': 6,'name': "sakthi",'age':22},
    {'roll_no': 7,'name': "praveen",'age':21},
    {'roll_no': 8,'name': "sunil",'age':20},
    {'roll_no': 9,'name': "saambu",'age':21},
    {'roll_no': 10,'name': "vijay",'age':22},
    {'roll_no': 11,'name': "vignesh",'age':23},
    {'roll_no': 12,'name': "noone",'age':25},
    {'roll_no': 13,'name': "hithere",'age':23}
]

x=mycol.insert_many(stud_list)
print(x.inserted_ids,end='')

# stud_list = [
#     {'_id':21,'roll_no': 1, 'name': "vijay", 'age': 21},
#     {'_id':22,'roll_no': 2, 'name': "goutham", 'age': 21},
#     {'_id':23,'roll_no': 3, 'name': "karthick", 'age': 23},
#     {'_id':24,'roll_no': 4, 'name': "nithil", 'age': 22},
#     {'_id':25,'roll_no': 5, 'name': "shyam", 'age': 25},
#     {'_id':26,'roll_no': 6, 'name': "sakthi", 'age': 22},
#     {'_id':27,'roll_no': 7, 'name': "praveen", 'age': 21},
#     {'_id':28,'roll_no': 8, 'name': "sunil", 'age': 20},
#     {'_id':29,'roll_no': 9, 'name': "saambu", 'age': 21},
#     {'_id':30,'roll_no': 10, 'name': "vijay", 'age': 22},
#     {'_id':31,'roll_no': 11, 'name': "vignesh", 'age': 23},
#     {'_id':32,'roll_no': 12, 'name': "noone", 'age': 25},
#     {'_id':33,'roll_no': 13, 'name': "hithere", 'age': 23}
# ]
# x = mycol.insert_many(stud_list)
print(x.inserted_ids, end='')
for i in x.inserted_ids:
    print(i)
 
##finding one spexcific element in the list:

val = mycol.find_one()
print(val)