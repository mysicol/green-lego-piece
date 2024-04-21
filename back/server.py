from flask import Flask, jsonify, request
from flask_cors import CORS
from Driver import Driver, Modes

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
    print(verifact['verifact'])
    
    driver = Driver(verifact['verifact'])
    data_table, summaries = driver.go(mode=Modes.TESTING)

    # example json data
    head_articles = []
    articles = []
    for i in range(2):
        head_articles.append({
            "id": i,
            "title": shorten_title(data_table['title'][i]),
            "reliability": data_table['reliability'][i],
            "bias": data_table['bias'][i],
            "relevance": data_table['relevance'][i],
            "summary": summaries[i],
            "url": data_table['raw_links'][i],
            "source": data_table['sources'][i],
        },)
    if (len(data_table) > 2):
        for i in range(2, len(data_table)):
            articles.append({
                        "id": i,
                        "title": shorten_title(data_table['title'][i]),
                        "reliability": data_table['reliability'][i],
                        "bias": data_table['bias'][i],
                        "relevance": data_table['relevance'][i],
                        "url": data_table['raw_links'][i],
                        "source": data_table['sources'][i],
                    },)
    print(articles)
    return jsonify( 
        {
            "summary": {
                "average": sum([int(i) for i in data_table['bias']]) / len(data_table['bias']),
                "reliability": max(data_table['reliability']),
                "headArticles": head_articles,
                "articles": articles,
            }
        }
    )


def shorten_title(title):
    if len(title) > 60:
        return title[:60] + "..."
    else:
        return title

if __name__ == "__main__":
    # debug = True so we can see live updates while developing
    app.run(debug=True, port=3000)