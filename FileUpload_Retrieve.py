from flask import Flask
from flask_pymongo  import PyMongo
from flask import jsonify, request



app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://Karan_Goel:karanphone123@cluster0-x0v9m.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)





@app.route('/create', methods=['POST'])
def create():
    _json = request.json
    print(_json)
    
    if 'profile_image' in request.files:
        profile_image = request.files['profile_image']
        mongo.save_file(profile_image.filename, profile_image)
        mongo.db.users.insert({'username': request.form.get('username'), 'profile_image_name': profile_image.filename})



        resp = jsonify("User Added Successfully")

        return resp




#@app.route('/delete/<username>', methods=['DELETE'])
#def delete_user(filename):
    #mongo.db.user.delete_one({'username': request.form.get('username' or 'profile_image')})


   # return 'Deleted!'


# if __name__ == '__main__':




app.run( host='127.0.0.3', debug=True)