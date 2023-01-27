#!flask/bin/python
from flask import Flask, jsonify, request, json
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://"+os.getenv("MONGODB_ADMINUSERNAME")+":"+os.getenv("MONGODB_ADMINPASSWORD")+"@"+os.getenv("MONGO_DB_URL")+"/snspost"
db_client = PyMongo(app)
db = db_client.db

# posts = [
#     {
#         'user': u'Tim Berner',
#         'msg': u'La Divina Commeida'
#     },
#     {
#         'user': u'Tim Berner',
#         'msg': u'Ernest Hemingway'
#     },
#     {
#         'user': u'Tim Berner',
#         'msg': u'Ernest Hemingway'
#     }
# ]

@app.route('/', methods=['GET'])
def get_init():
    return jsonify({'HTTP':"200 connected"})

@app.route('/posts', methods=['GET'])
def get_posts():
    # output = list()
    posts = db.posts.find()
    # return jsonify({'posts': posts})
    return jsonify([post for post in posts])


@app.route('/posts', methods=['POST'])
def add_post():
    # posts.append(json.loads(request.data))
    db.posts.insert_one(json.loads(request.data))
    return jsonify({'HTTP Code': "200"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
