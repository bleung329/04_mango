from pymongo import MongoClient

c = MongoClient('lisa.stuy.edu')

db = c.test

coll = db.restaurants

def find_by_borough(bor):
    return coll.find({'borough':bor})

def find_by_zip(zip):
    stri = str(zip)
    return coll.find({'address.zipcode':stri})

    
print(find_by_zip(10282))
