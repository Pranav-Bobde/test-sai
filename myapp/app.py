# setup a flask app with / endpoint

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)