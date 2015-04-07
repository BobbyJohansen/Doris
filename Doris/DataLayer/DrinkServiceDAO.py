from datetime import datetime
from flask import Flask, request
from flask.ext.mongokit import MongoKit, Document




def insertDocument():
    return 'asd'
    













#************************TESTING ABOVE THIS LINE**************************************
global db
global app
#global connection
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
MONGODB_DATABASE = 'Drinks'

class Drink(Document):
    __collection__='testData'
    __database__= MONGODB_DATABASE
    structure = {
        'title':basestring,
        'text':basestring,
        'created':datetime,}
    required_fields = ['title','created']
    default_values = {'created':datetime.utcnow}
    use_fot_notation = True

def insertDrink(request):
    


def insertDrinkJSON(json_object):
    db['testData'].insert(json_object)
    return 'completed : ' + str(json_object)

def getAllDrinks():
    drinks = db.Drink.find()
    return drinks

def initDB(drinkService):
    global db
    global app
    #  global connection
    app = drinkService
    db = MongoKit(drinkService)
    #connection = Connection()
    db.register([Drink])
