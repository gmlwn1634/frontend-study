from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert/ find / update / delete

# insert
doc = {'name':'bobby','age':31}
db.users.insert_one(doc)

# find
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# for person in same_ages:
#     print(person)

# find_one
# user = db.users.find_one({'name':'bobby'})
# print(user['age'])


# update
# db.users.update_one({'name':'bobby'},{'$set':{'age':21}})
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# delete
# db.users.delete_one({'name':'bobby'})
# db.users.delete_many({'name':'bobby'})

