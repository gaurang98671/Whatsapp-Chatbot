import pymongo

def place_order(number, order):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['mydatabase']
    mycol = mydb['orders']
    mydict={
            'phone': number,
            'orders': order
            }
    mycol.insert_one(mydict)
    print('Order placed')

def view_order():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['mydatabase']
    mycol = mydb['orders']
    for i in mycol.find():
        print(i)

def find_order(phone):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['mydatabase']
    mycol = mydb['orders']
    x=mycol.find_one({'phone': phone})
    print(x)

def delete_orders(phone):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient['mydatabase']
    mycol = mydb['orders']
    mycol.delete_one({'phone': phone})
    print('Order deleted')

