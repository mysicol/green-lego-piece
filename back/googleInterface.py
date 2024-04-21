# from search_engine_parser import BingSearch as searchEngineType
from serpapi import GoogleSearch as serpEngine
from APIKeys import APIKeys
import pickle

class SearchEngine:

    def __init__(self):
        self.__titles = []
        self.__query = "NullQuery"
        self.__links = []
        self.__desc = []
        APIKeys.set_var("SERP_API_KEY")

    def _clean_up_link(self, link):
        """ Helper function to clean up the link 

        Parameters:
        -----------------
         - link {string}: 

        Return:
        -----------------
         - clean_link {string}: Link stripped to .name.domain 
        """

        main_link = link.split("/")[2]
        if len(main_link.split('.')) > 2:
            main_link = main_link.split('.', 1)[1]
        return main_link

    def make_query(self, query):
        """ Makes given query to Google Search result. Stores results in class lists.
        Query results are saved as titles, descriptions, and links

        Parameters:
        -----------------
         - query {string}: Search query to look for
        """
        self.__query = query
        self.__titles = []
        self.__links = []
        self.__desc = []

        search_params = {
            "api_key": APIKeys.get_key("SERP_API_KEY"),
            "engine": "google",
            "q": query,
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en",
            "tbm": "nws",
            "num": "20"
            }
        
        search = serpEngine(search_params)
        results = search.get_dict()

        for news_result in results['news_results']:
            self.__titles.append(news_result['title'])
            self.__desc.append(news_result['snippet'])
            self.__links.append("." + self._clean_up_link(news_result['link']))

        self.__serialize_results()

        return (self.__titles, self.__desc, self.__links)
    
    def __serialize_results(self):
        data = (self.__titles, self.__desc, self.__links)
        pickle_name = '_'.join(self.__query.split(" ")) + ".pkl"
        with open(pickle_name, 'wb') as f:
            pickle.dump(data, f)
    
    def prune_results(self, relevance_ratings, relevance_threshold):
        """ Removes specific stored results from last query based on relevance

        Parameters:
        -----------------
         - relevance_ratings {list}: List of relevance ratings on a scale from X-Y
         - relevance_threshold {int}: Number representing mininum relevance to be kept. X <= relevance_threshold <= Y
        """
        if self.__query == "NullQuery":
            print("Not pruning, no query has been made")
            return
        
        indexes_to_remove = []
        for i, relevance in enumerate(relevance_ratings):
            if relevance < relevance_threshold:
                print(i, relevance)
                indexes_to_remove.append(i)

        indexes_to_remove.reverse()
        for i in indexes_to_remove:
            self.__titles.pop(i)
            self.__desc.pop(i)
            self.__links.pop(i)

    def get_titles(self):
        """Returns list of titles as strings based on last query

        Returns:
        -----------------
        - self.__titles {list : string} : List of result titles as strings
        """
        return self.__titles
    
    def get_title(self, index):
        """Return title of result from last query with given index as a string

        Parameters:
        -----------------
        - index {int} : Index of title to return

        Returns:
        -----------------
        - self.__titles[i] {string} : Result title at index, None if index > len(self.__titles)
        """
        if index < len(self.__titles):
            return self.__titles[index]
        else:
            return None
    
    def get_descriptions(self):
        """Returns list of descriptions as strings based on last query

        Returns:
        -----------------
        - self.__desc {list : string} : List of result descriptions as strings
        """
        return self.__desc
    
    def get_description(self, index):
        """Return description of result from last query with given index as a string

        Parameters:
        -----------------
        - index {int} : Index of description to return

        Returns:
        -----------------
        - self.__desc[i] {string} : Result description at index
        """
        if index < len(self.__desc):
            return self.__desc[index]
        else:
            return ""
    
    def get_links(self):
        """Returns list of links as strings based on last query
        
        Returns:
        -----------------
        - self.__links {list : string} : List of result links as strings
        """
        return self.__links
    
    def get_link(self, index):
        """Return link of result from last query with given index as a string

        Parameters:
        -----------------
        - index {int} : Index of link to return

        Returns:
        -----------------
        - self.__links[index] {string} : Result link at index
        """
        if index < len(self.__links):
            return self.__links[index]
        else:
            return None
    
    def get_last_query(self):
        """Return last query as a string

        Returns:
        -----------------
        - self.__query {string} : Last made query as a string
        """
        return self.__query
    
    def get_num_results(self):
        """Returns number of results received from search query
        
        Returns:
        -----------------
        - len(self.__titles) {int} : Length of titles, should be the number of results as each result has a title
        """
        return len(self.__titles)



if __name__ == "__main__":

    # Just some simple test code to show use of functions
    se = SearchEngine()

    print(se._clean_up_link("https://stackoverflow.com/questions/39875629/how-to-use-strip-in-map-function"))

    searching = True
    while searching:
        query = input("What do you want to search? ")

        if query == "":
            exit()

        se.make_query(query)
        print()

        for i in range(se.get_num_results()):
            print("Result #", (i+1))
            print("Title:", se.get_title(i))
            print("Summary: ", se.get_description(i))
            print("Link: ", se.get_link(i))
            print("\n")

