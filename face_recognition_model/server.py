from flask import Flask, request
from register_user import register_user

app = Flask(__name__)
@app.route('/api/register_face', methods=['GET'])
def register_face():
    register_user("sidd", 5, "people.json")
    return 'registered'

if __name__ =='__main__':  
    app.run()  