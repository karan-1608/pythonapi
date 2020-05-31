from flask import Flask, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config[
    'MONGO_URI'] = 'mongodb+srv://Karan_Goel:karanphone123@cluster0-x0v9m.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)


@app.route('/')
def index():
    return '''
    <form method="POST" action="/create" enctype="multipart/form-data">
        <input type="text" name="username">
        <input type="file" name="profile_image">
        <input type="submit">
    </form>

    <form method = "GET" action="/file/<filename>" enctype = "multipart/form-data">          
      <input type = "text" name = "profile_image">
      <input type = "submit">
    </form>

'''


@app.route('/create', methods=['POST'])
def create():
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username': request.form.get('username'), 'profile_image_name': profile_image.filename})

    return 'Done!'


@app.route('/file/<filename>')
def file(filename):
    return mongo.send_file(request.form.get('username' or 'profile_image'))


@app.route('/profile/<username>')
def profile(username):
    user = mongo.db.user.find_one_or_404({'username': username})
    return f'''
        <h1>{username}</h1>
        <img src="{url_for('file', filename=user['profile_image_name'])}">
        '''


# @app.route('/delete/<username>', methods=['DELETE'])
# def delete_user(filename):
# mongo.db.user.delete_one({'username': request.form.get('username' or 'profile_image')})


# return 'Deleted!'


# if __name__ == '__main__':


app.run(host='127.0.0.2', debug=True)