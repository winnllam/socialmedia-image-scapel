from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
CORS(app)

### swagger ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "socialmedia-image-scapel"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger ###

@app.route('/dribbble/', methods=['GET'])
def dribbble():
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
    return "<h1>Social Media Image API</h1><p>This is an API that extracts thumbnail URLs of shots made by a user on different media platforms</p>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
