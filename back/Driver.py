from flask import jsonify
from googleInterface import SearchEngine
from dataset import DatasetContext
from Similarity import Similarity
from URLToArticle import URLToArticle
from GPTInterface import GPTInterface
import pandas as pd
import pickle
from enum import Enum

class Modes(Enum):
    TESTING = 0
    RUNNING = 1

class Driver:
    def __init__(self, query):
        self.__query = query
        
    def load_willdumb():
        import pickle
        
        with open('data/Trump_goes_to_jail.pkl', 'rb') as f:
            data = pickle.load(f)

            titles, desc, links, raw_links = data

        return titles, desc, links, raw_links

    def go(self, mode=Modes.TESTING):

        data_dictionary = DatasetContext("news.csv").get_dictionary()
        news_urls = data_dictionary.keys()

        # searcher = SearchEngine()
        # searcher.makeQuery()

        # titles = searcher.get_titles()
        # descriptions = searcher.get_description()
        # links = searcher.get_links()

        if (mode == Modes.TESTING):
            titles, desc, links, raw_links = Driver.load_willdumb()
        else:
            searcher = SearchEngine()
            searcher.makeQuery()

            titles = searcher.get_titles()
            desc = searcher.get_description()
            links = searcher.get_links()
            
            similarity = Similarity(self.__query)
        
        data = {'title': [], 'desc': [], 'links': [], 'raw_links': [], 'bias': [], 'reliability': [], 'relevance': []}

        for i in range(len(links)):
            if links[i] in news_urls:
                # Appending article information for known sources
                data['title'].append(titles[i])
                data['desc'].append(desc[i])
                data['links'].append(links[i])
                data['raw_links'].append(raw_links[i])
                
                # Adding news source information
                node = data_dictionary.get(links[i])
                data['bias'].append(node.get_bias_value())
                data['reliability'].append(node.get_reliability_value())
                
                # Determining similarity
                if (mode == Modes.TESTING):
                    data['relevance'].append('1')
                else:
                    data['relevance'].append(similarity.get_rating(titles[i]))

        data_table = pd.DataFrame(data)
        
        data_table = data_table.sort_values(by='reliability')
        
        gpt = GPTInterface()
        summaries = []
        
        if (mode == Modes.TESTING):
            article = Driver.load_article("data/article1.pkl")
        else:
            reader = URLToArticle(raw_links[0])
            article = reader.read()
        #Driver.save_article(article, "data/article1.pkl")
        summaries.append(gpt.get_summary(article))
        if (mode == Modes.TESTING):
            article = Driver.load_article("data/article2.pkl")
        else:
            reader = URLToArticle(raw_links[0])
            article = reader.read()
        #Driver.save_article(article, "data/article2.pkl")
        summaries.append(gpt.get_summary(article))
        
        return data_table, summaries
    
    def save_article(article, filename):
        with open(filename, 'wb') as file:
            pickle.dump(article, file)
        file.close()
        
    def load_article(filename):
        result = ""
        with open(filename, "rb") as file:
            result = pickle.load(file)
        file.close()
        return result

    def create_json(data_table, summaries):
        articles = []
        for i in range(len(data_table)):
            articles.append({
                        "id": i,
                        "title": data_table['title'][i] ,
                        "reliability": data_table['reliability'][i],
                        "bias": data_table['bias'][i],
                    },)
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
                "articles": articles
            }
        }
        )