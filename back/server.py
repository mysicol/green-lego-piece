from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route("/api/example", methods=['GET'])
def example():
    return jsonify(
        {
            "data": {
                "reliability": 50,
                "bias": 70,
            }
        }
    )

@app.route("/api/input", methods=['POST'])
def input():
    verifact = request.json

    print(verifact) # TODO remove

    # TODO turn verifact into a search query, make the search, and then return json below 

    # example json data
    return jsonify( 
        {
            "summary": {
                "average": 50,
                "reliability": 70,
                "headArticles": [
                    {
                        "id": 0,
                        "title": "Title",
                        "reliability": 60,
                        "bias": 50,
                        "summary": "A summary",
                    },
                    {
                        "id": 1,
                        "title": "22222",
                        "reliability": 2,
                        "bias": 20,
                        "summary": "2sum2",
                    },
                ],
                "articles": [
                    {
                        "id": 0,
                        "title": "Another Title",
                        "reliability": 30,
                        "bias": 20,
                    },
                ],
            }
        }
    )

if __name__ == "__main__":
    # debug = True so we can see live updates while developing
    app.run(debug=True, port=3000)