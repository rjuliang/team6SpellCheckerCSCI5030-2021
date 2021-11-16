from flask import Flask, jsonify, request
from spellCheck import *

#export FLASK_APP=get-localhost.py
#python -m flask run

app = Flask(__name__)

@app.route('/process')
def processSpellCheck():
    phrase = request.args.get('phrase', None)
    language = request.args.get('lng', None)

    if phrase and language:
        print('phrase: '+phrase)
        errorList = checkPhrase(phrase)
        return jsonify(errorList)
    else:
        return 'Missing either parameters'