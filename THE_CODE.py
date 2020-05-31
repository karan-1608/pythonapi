from flask import Flask, request
from flask_pymongo import PyMongo
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Karan_Goel:<password>@cluster0-x0v9m.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)
CORS(app)


@app.route('/create', methods=['POST'])
def create():
    _file = request.files['profile']
    _file1 = request.form['name']

    if _file1 and _file and request.method == 'POST':
        mongo.save_file(_file.filename, _file)
        mongo.db.users.insert({'_id': _file1, 'username': _file1, 'profile_image_name': _file.filename})
    resp = jsonify("User Added Successfully")
    return resp


@app.route('/file', methods=['GET'])
def file():
    _json = request.args.get('photo')
    w = mongo.db.users.find_one(_json)
    s = w['profile_image_name']
    return mongo.send_file(str(s))


if __name__ == '__main__':
    app.run(host='127.0.0.5')


