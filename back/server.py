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

    print(verifact) # TODO remove, structure of verifact is: { verifact: "string" }

    # TODO turn verifact into a search query, make the search, and then return json below 

    # example json data
    return jsonify( 
        {
            "summary": {
                "average": 25,
                "reliability": 70,
                "headArticles": [
                    {
                        "id": 0,
                        "title": "Are cats real?",
                        "reliability": 80,
                        "bias": 12,
                        "relevance": 70,
                        "summary": "This is a really great summary about whether or not cats are real. Turns out, they are fake. Just like birds.",
                    },
                    {
                        "id": 1,
                        "title": "Old people, true or false?",
                        "reliability": 2,
                        "bias": 30,
                        "relevance": 20,
                        "summary": "This is a semi-reliable article. We may never know the answer to this age-old question. It is almost as controversial as the debate on the existence of cats, or even more pressing, the existence of birds.",
                    },
                ],
                "articles": [
                    {
                        "id": 0,
                        "title": "Another Title",
                        "reliability": 30,
                        "bias": 20,
                        "relevance": 12,
                    },
                ],
            }
        }
    )

if __name__ == "__main__":
    # debug = True so we can see live updates while developing
    app.run(debug=True, port=3000)