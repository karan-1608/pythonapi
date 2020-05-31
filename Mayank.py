from flask import Flask, request, url_for
from flask_pymongo import PyMongo
import json
import requests
from urllib import request

app = Flask(__name__)
app.config[
    'MONGO_URI'] = 'mongodb+srv://MayankChauhan:sms123456789@cluster0-y9jba.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/create', methods=['POST'])
def create():


# print('helllo')
response = requests.post("http://127.0.0.2:5000/create")
print(response.json())
if 'profile_image' in request.files:
    profile_image = request.files['profile_image']
    mongo.save_file(profile_image.filename, profile_image)
    mongo.db.data.insert({'username': request.form.get('username'), 'profile_image_name': profile_image.filename})
return 'Done!'


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(request.form.get('username' or 'profile_image'))


@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.data.find_one_or_404({'username': username})
    return f'''
        <h1>{username}</h1>
        <img src="{url_for('file', filename=user['profile_image_name'])}">
        '''


if __name__ == '__main__':
    app.run(host='127.0.0.2')

