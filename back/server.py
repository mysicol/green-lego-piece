from flask import Flask, jsonify
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

if __name__ == "__main__":
    # debug = True so we can see live updates while developing
    app.run(debug=True, port=3000)