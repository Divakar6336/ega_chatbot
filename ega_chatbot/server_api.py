from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import requests

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def hello_world():
    # user_id
    args = request.args
    print (args) # For debugging
    uid = args['user_id']
    pwd = args['password']
    if uid=='admin' and pwd=='12345':
        return jsonify({"data":"Flask API Called"})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8081)

