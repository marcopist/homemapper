from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def fetch_polygon():
    paylaod = request.get_json()
    return paylaod