#!flask/bin/python
from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# app.config["MONGO_URI"] = "mongodb://localhost:27017/<DBNAME>"
# db = PyMongo(app).db

posts = [
    {
        'user': u'Tim Berner',
        'msg': u'La Divina Commeida'
    },
    {
        'user': u'Tim Berner',
        'msg': u'Ernest Hemingway'
    },
    {
        'user': u'Tim Berner',
        'msg': u'Ernest Hemingway'
    }
]

@app.route('/', methods=['GET'])
def get_posts():
    output = list()
    # posts = db.
    return jsonify({'posts': posts})


@app.route('/postings', methods=['POST'])
def add_post():
    posts.append(json.loads(request.data))
    return jsonify({'posts': posts})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
