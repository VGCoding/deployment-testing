from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/route')
def index():
    return {
        "tot":"run suc"
    }
@app.route('/')
def serve():
    return {"name":"Naam"};

if __name__=='__main__':
    app.run()
