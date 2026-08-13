# package name: flask
# class name  : Flask
from flask import Flask

# create a flask application instance
app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_get():
    return "welcome to my first flask app"

@app.route('/', methods=['POST'])
def root_post():
    return "POST /"

# run the flask server
app.run(
    # the server can be reached from network client
    host="0.0.0.0",

    # custom port
    port=5200,

    # debug flag (True: development, False: Production)
    debug=True
)
