''' Class for connecting and interacting with the dataset.'''
import csv

''' The Data Node that each row of data will be saved into.'''
class DataNode:
	def __init__(self, name, domain, reliability_value, bias_value):
		self.name = name 
		self.domain = domain
		self.reliability_value = reliability_value
		self.bias_value = bias_value

	def __str___(self):
		return (self.domain, self.name, self.reliability_value, self.bias_value)

	def get_domain(self):
		return self.domain
	
	def get_name(self):
		return self.name

	def get_reliability_value(self):
		return self.reliability_value

	def get_bias_value(self):
		return self.bias_value

class DatasetContext:
	def __init__(self, path):
		self.sourcesDictionary = self.init_data(path)

	def init_data(self, pathName):
		sources = self.parseFile(pathName)
		return self.createDict(sources)

	def parseFile(self, pathName):
		""" Parses the file found from the given path name.
		Returns a regular list of DataNode objects.

        Parameters:
        -----------------
         - pathName {string}: The relative path of the csv data file
        """
		sources = []
		with open(pathName, 'r') as csvFile:
			csvReader = csv.reader(csvFile)

			# Iterate over each row in the CSV file
			for row in csvReader:
				name = row[0]
				domain = row[3]
				reliability_value = row[1]
				bias_value = row[2]
				sources.append(DataNode(name, domain, reliability_value, bias_value))
		return sources
	
	def createDict(self, source_list):
		""" Creates a dictionary of the data where the key is the source domain 
		and the value is the DataNode object holding all data for that source.
		Returns the new dictionary.

		Parameters:
		----------------
		 - source_list {list}: The list of DataNodes to be made into a dictionary
		"""
		sources = {}	
		for source in source_list:	
			sources[source.get_domain()] = source
		return sources
	
	def get_dictionary(self):
		return self.sourcesDictionary
	
	def get_source(self, queryDomain):
		return self.sourcesDictionary.get(queryDomain)


if __name__ == "__main__":

	dataDictionary = DatasetContext("news.csv").get_dictionary()

	''' THE FOLLOWING WAS USED FOR TESTING'''
	sampleDomain = ".newstarget.com"
	sourceNode = dataDictionary.get(sampleDomain)
	print("name", sourceNode.get_name())
	print("r-value", sourceNode.get_reliability_value())
	print("bias", sourceNode.get_bias_value())