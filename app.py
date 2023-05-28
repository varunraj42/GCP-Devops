from flask import Flask
app = Flask(__name__)

@app.route('/hello_world', methods=['GEt'])
def hello_world():
    return 'Hello, Flask Application'