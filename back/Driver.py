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

    def go(self, mode=Modes.TESTING):
        if (mode == Modes.TESTING):
            return self.__goTest()
        else:
            return self.__goRun()
        
    def __goTest(self):
        return Driver.__load("data/testrun.pkl")
    
    def __goRun(self):
        data_dictionary = DatasetContext("news.csv").get_dictionary()
        news_urls = data_dictionary.keys()

        searcher = SearchEngine()
        searcher.make_query(self.__query)

        titles = searcher.get_titles()
        desc = searcher.get_descriptions()
        links = searcher.get_links()
        raw_links = searcher.get_raw_links()
        
        similarity = Similarity(self.__query)
        
        data = {'title': [], 'desc': [], 'links': [], 'raw_links': [], 'bias': [], 'reliability': [], 'relevance': [], 'sources': []}

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
                data['sources'].append(node.get_name())
                
                # Determining similarity    
                relevance = similarity.get_rating(titles[i])
                data['relevance'].append(Driver.scale_relevance(relevance))

        data_table = pd.DataFrame(data)
        print(data_table)
        data_table = data_table.sort_values(by='reliability', ascending=False)
        data_table.reset_index(drop=True, inplace=True)
        print(data_table)
        
        gpt = GPTInterface()
        summaries = []

        reader = URLToArticle(raw_links[0])
        article = reader.read()
        summaries.append(gpt.get_summary(article))
        
        reader = URLToArticle(raw_links[1])
        article = reader.read()
        summaries.append(gpt.get_summary(article))
        
        print(data_table['title'])
        Driver.__save(data_table, summaries, "data/testrun.pkl")
        return data_table, summaries
    
    def __save(data_table, summaries, filename):
        with open(filename, 'wb') as file:
            pickle.dump([data_table, summaries], file)
        file.close()
        
    def __load(filename):
        result = ""
        with open(filename, "rb") as file:
            result = pickle.load(file)
        file.close()
        return result
    
    def scale_bias(bias):
        return str(math.floor(float(bias) / 40 * 100))
    
    def scale_relevance(relevance):
        return str(math.floor(float(relevance) / 1 * 100))
    
    def scale_reliability(reliability):
        return str(math.floor(float(reliability) / 50 * 100))
