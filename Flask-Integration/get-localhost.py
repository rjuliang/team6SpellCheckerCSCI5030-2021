from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from spellCheck import *
import json

#export FLASK_APP=get-localhost.py
#python -m flask run

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/process')
@cross_origin()
def processSpellCheck():
    phrase = request.args.get('phrase', None)
    language = request.args.get('lng', None)


    if phrase and language:
        print('phrase: '+phrase)
        errorList = checkPhrase(phrase, language)

        return jsonify({'phrase': phrase, "suggestions":errorList})
    else:
        return 'Missing either parameters'