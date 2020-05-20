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

def insertarCarrito(idCliente, idTrack, subtotal):
    mydict = {"idCart": idCliente, "idCliente", idCliente, "idTrack": idTrack, "subtotal": subtotal}
    shopping.insert_one(mydict)

def buscarCarrito(idCliente)
    resultado = shopping.find({"idCliente": idCliente})
    
