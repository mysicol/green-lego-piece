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
	# data should be a dictionary
	def __init__(self, data):
		self.data = data

def parseFile(pathName):
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
		

if __name__ == "__main__":
	path = "News.csv"
	# parseFile returns a list of DataNodes. 
	source_list = parseFile(path)

	# Create a dictionary sources.  [String domainName: DataNode]
	sources = {}
	print("for source in sourcelist")
	for source in source_list:	
		sources[source.get_domain()] = source

	
	datasetContext = DatasetContext(sources)

	''' THE FOLLOWING WAS USED FOR TESTING
	sampleDomain = ".newstarget.com"
	sourceNode = sources[sampleDomain]
	print("name", sourceNode.get_name())
	print("r-value", sourceNode.get_reliability_value())
	print("bias", sourceNode.get_bias_value())'''