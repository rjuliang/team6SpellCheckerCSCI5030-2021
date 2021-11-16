from flask import Flask, jsonify, request
from spellCheck import *

#export FLASK_APP=test1.py
#flask run

app = Flask(__name__)

@app.route('/process')
def dataGet():
    phrase = request.args.get('phrase', None)
    language = request.args.get('lng', None)

    if phrase and language:
        print('phrase: '+phrase)
        errorList = checkPhrase(phrase)
        print('After error list')
        return jsonify(errorList)
    else:
        return 'Missing either parameters'