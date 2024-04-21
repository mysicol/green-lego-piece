import requests
from back.APIKeys import APIKeys

VAR_NAME = 'NINJAS_API_KEY'

class Similarity:    
    def __init__(self, query):
        self.__query = query
        self.__api_url = 'https://api.api-ninjas.com/v1/textsimilarity'
        
        APIKeys.set_var(VAR_NAME)
        self.__apikey = APIKeys.get_key(VAR_NAME)

    def getRating(self, article):
        body = { 'text_1': self.__query, 'text_2': article }
        response = requests.post(self.__api_url, headers={'X-Api-Key': self.__apikey}, json=body)
        
        if response.status_code == requests.codes.ok:
            return float(response.text.split(" ")[1][:-1])
        else:
            print("Error:", response.status_code, response.text)