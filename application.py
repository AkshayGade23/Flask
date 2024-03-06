from urllib import response
from flask import Flask, jsonify, request
import nltk
import text2emotion as text

application = Flask(__name__)

@application.route('/feeling')
def feelingController():
    response = {}
    response['query'] = str(request.args['query'])
    response['output'] = text.get_emotion(response['query'])
    response['emotion'] = max(response['output'], key= lambda x: response['output'][x])
    if response['emotion'] == 'Surprise':
        response['emotion'] = 'Happy'
    return jsonify(response)


@application.route('/feeling')
def hello():
    return "Hello Geeta APP"

if __name__ == '__main__':
    application.run()

nltk.download('omw-1.4')    # To make the nltk up-to-date