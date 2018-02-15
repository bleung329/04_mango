from pymongo import MongoClient
from bson import json_util
import urllib2

c = MongoClient('lisa.stuy.edu')

mongJesus = c.test
db = c.test

coll = db.restaurants

collie = mongJesus.coll1
data = "http://api.giphy.com/v1/gifs/search?q=cats&api_key=dc6zaTOxFJmzC"
data2 = urllib2.urlopen(data)
response = json_util.loads(data2.read())
collie.insert_one(response)

def cprint(curse):
    for item in curse:
        print item 


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

'''
cprint(find_by_borough('Brooklyn'))
cprint(find_by_zip(10282))
cprint(find_by_zipgrade(10282,"a"))
cprint(find_by_zipgrade(10282,10))
'''

def find_by_rating(rat):
    return collie.find({'data.0.rating':rat})

cprint(find_by_rating('g'))
