from flask import app,Flask,jsonify

server = Flask(__name__)

@server.route("/",methods=['GET'])
def login():
    return jsonify(dict())

server.run(port=9090,debug=True)