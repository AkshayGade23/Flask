from urllib import response
from flask import Flask, jsonify, request
import nltk
import text2emotion as text

app = Flask(__name__)

@app.route('/feeling')
def feelingController():
    response = {}
    response['query'] = str(request.args['query'])
    response['output'] = text.get_emotion(response['query'])
    response['emotion'] = max(response['output'], key= lambda x: response['output'][x])
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

nltk.download('omw-1.4')    # To make the nltk up-to-date