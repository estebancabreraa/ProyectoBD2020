import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]

shopping = mydb["shopping-cart"]

compra = mydb["compra"]

mydict = {"idCart": 2, "idClient": 0, "idTrack": 1, "subtotal": 0.99}

myquery = { "idClient": 0}

x = shopping.insert_one(mydict)
#DELETE
#shopping.delete_many(myquery)

for x in shopping.find(myquery):
  print(x)
