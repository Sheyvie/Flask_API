from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<b> My first Flask application in action!<b>"
#def index():
    #return jsonify(message="Hello World")
