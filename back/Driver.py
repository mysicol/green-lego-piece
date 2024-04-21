from flask import jsonify
from googleInterface import SearchEngine
from dataset import DatasetContext
from Similarity import Similarity
from URLToArticle import URLToArticle
from GPTInterface import GPTInterface
import pandas as pd
import pickle
import math
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
                data['bias'].append(Driver.scale_bias(node.get_bias_value()))
                data['reliability'].append(Driver.scale_reliability(node.get_reliability_value()))
                
                # Determining similarity
                if (mode == Modes.TESTING):
                    relevance = '0.01'
                else:
                    relevance = similarity.get_rating(titles[i])
                data['relevance'].append(Driver.scale_relevance(relevance))

        data_table = pd.DataFrame(data)
        
        data_table = data_table.sort_values(by='reliability')
        
        gpt = GPTInterface()
        summaries = []
        
        if (mode == Modes.TESTING):
            article = Driver.load_article("data/article1.pkl")
            summaries.append("summary1")
        else:
            reader = URLToArticle(raw_links[0])
            article = reader.read()
            summaries.append(gpt.get_summary(article))
        #Driver.save_article(article, "data/article1.pkl")
        if (mode == Modes.TESTING):
            article = Driver.load_article("data/article2.pkl")
            summaries.append("summary2")
        else:
            reader = URLToArticle(raw_links[0])
            article = reader.read()
            summaries.append(gpt.get_summary(article))
        #Driver.save_article(article, "data/article2.pkl")
        
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
    
    def scale_bias(bias):
        return str(math.floor(float(bias) / 40 * 100))
    
    def scale_relevance(relevance):
        return str(math.floor(float(relevance) / 0.1 * 100))
    
    def scale_reliability(reliability):
        return str(math.floor(float(reliability) / 50 * 100))