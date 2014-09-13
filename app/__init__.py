from flask import Flask, Response
import requests

# Create a Flask application with config
app = Flask(__name__)

@app.route('/<path:url>')
def main(url):
    return Response(requests.get(url), mimetype='application/pdf')
