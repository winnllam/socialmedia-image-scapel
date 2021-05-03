from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
CORS(app)


@app.route('/get_img_urls/', methods=['GET'])
def respond():
    # Retrieve the username from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    source = requests.get(f"https://dribbble.com/{name}").text
    soup = BeautifulSoup(source, 'lxml')
    thumbnails = soup.find_all('div', class_='js-shot-thumbnail-base')

    urls = []

    for tn in thumbnails:
        urls.append(tn.find('img')['src'])

    print(urls)

    response = {}

    # Check if user sent a name at all
    if not name:
        response["error"] = "no name found, please send a name."
    else:
        response["urls"] = urls

    # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
