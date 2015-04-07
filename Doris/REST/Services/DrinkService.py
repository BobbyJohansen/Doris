#Configure Logging
import logging
from logging import Formatter, FileHandler


#Application imports
from flask import Flask, request
from flask.ext.mongokit import MongoKit, Document
import json
from json import JSONEncoder

#import DrinkService DAO
import DrinkServiceDAO

#Define the application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def testing():
    return insertIntoDB()

@app.route('/hello',methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/welcome',methods=['GET'])
def welcome():
    return 'welcome you lazy bastard'

@app.route('/test',methods=['POST'])
def insert():
    json_object = json.loads(request.data)
    return json_object

@app.route('/insert',methods=['POST'])
def insertIntoDB():
    json_object = json.loads(request.data)
    app.logger.info('JSON RECIEVED ' + str(json_object))
    return DrinkServiceDAO.insertDrinkJSON(json_object)

@app.route('/insertdrink',methods=['POST'])
def insertDrinkIntoDB():
    return DrinkServiceDAO.insertDrinkJSON(request)

#*************TESTING ABOVE THIS LINE****************************

@app.route('/createdrink', methods=['POST'])
def createDrink():
    return 'not implemented yet i think'

@app.route('/listdrinks', methods=['GET'])
def listDrinks():
    return 'not implemented'


@app.route('/drink/<drink>', methods=['GET'])
def getDrink(drink):
    return 'not implemented'


@app.route('/drink2/<drink>', methods=['GET'])
def getDrink2(drink):
    return 'not implemented'












#************MAIN***********************************************

def initLogging():
    #initialize loggging
    logger = logging.getLogger('werkzeug')
    whandler = FileHandler('../log/drinkservice.log')
    whandler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    logger.addHandler(whandler)
    handler = FileHandler('../log/drinkservice.log')
    handler.setLevel(logging.INFO)
    handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(handler)

def initDB():
    DrinkServiceDAO.initDB(app)

if __name__ == '__main__':
    initLogging()
    initDB()
    app.debug=True
    app.run(host='0.0.0.0')

