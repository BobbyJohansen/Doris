" " " The REST Service Layer to access drinks from mongo. " " "
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
    
@app.route('/hello')
def helloWorld():
    return 'Hello World'
    