from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')

db = c.test

coll = db.restaurants

def find_by_borough(bor):
    return coll.find({'borough':bor})

def find_by_zip(zip):
    stri = str(zip)
    return coll.find({'address.zipcode':stri})

def find_by_zipgrade(zip, grd):
    strin = str(zip)
    return coll.find( { "$and": [ {'address.zipcode':strin}, {'grade':grd}]})

def find_by_zipscore(zip, scr):
    st = str(zip)
    scre = str(scr)
    return coll.find( { "$and": [ {'address.zipcode':st}, {'score': {"$lt": scre}}]})


print(find_by_borough('Brooklyn'))
print(find_by_zip(10282))
print(find_by_zipgrade(10282,"a"))
print(find_by_zipgrade(10282,10))
