from flask import Flask, request, jsonify
app = Flask(__name__)
# run_with_ngrok(app)
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/', methods=['POST'])
def key():
    data = request.get_json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()