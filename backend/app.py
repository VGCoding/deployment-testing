from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/route')
def index():
    return "run suc"
@app.route('/')
def serve():
    return "Naam";

