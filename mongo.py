import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["proyecto"]

shopping = mydb["shopping-cart"]

compra = mydb["compra"]

mydict = {"idCart": 1, "idClient": 1, "idTrack": 1, "subtotal": 0.99}


for x in shopping.find({},{"idTrack": 1}):
  print(x)
