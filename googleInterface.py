from search_engine_parser import GoogleSearch

class SearchEngine:

    def __init__(self):
        self.__titles = []
        self.__query = "NullQuery"
        self.__links = []
        self.__desc = []

    def makeQuery(self, query):
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

        search_args = (query, 1)
        gsearch = GoogleSearch()
        gresults = gsearch.search(*search_args)

        # Store results in easily accessible format
        self.__titles.extend(gresults['titles'])
        self.__links.extend(gresults['links'])
        self.__desc.extend(gresults['descriptions'])
    
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
        else :
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



if __name__ == "__main__":

    # Just some simple test code. Won't actually do anything since no query is made
    se = SearchEngine()

    print(se.get_last_query())
    print(se.get_description(1))
    print(se.get_link(1))
    print(se.get_title(1))
    se.prune_results([10, 5, 8], 8)

    print(se.get_titles())
    print(se.get_descriptions())
    print(se.get_links())