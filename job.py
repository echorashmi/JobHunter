#DB: Mongo
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jobdb"]
mycol = mydb["jobdb"]

myquery = {"_type": "JobDescription"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)