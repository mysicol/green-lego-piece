''' Class for connecting and interacting with the dataset.'''
import csv

''' The Data Node that each row of data will be saved into.'''
class DataNode:
	def __init__(self, domain, name, reliability_value, bias_value):
		self.domain = domain
		self.name = name 
		self.reliability_value = reliability_value
		self.bias_value = bias_value

	def get_domain(self):
		return self.domain
	
	def get_name(self):
		return self.name

	def get_reliability_value(self):
		return self.reliability_value

	def get_bias_value(self):
		return self.bias_value

class DatasetContext:
	def __init__(self, data):
		self.data = data

	def parseFile(self, pathName):
		print("trying to parse file")

		list_of_rows = []
		with open(pathName, 'r') as csvFile:
			csvReader = csv.reader(csvFile)

			# Iterate over each row in the CSV file
			for row in csvReader:
				# row is a string from the csv

				print("row: ", row)
				row_list = row.split("")
				list_of_rows.append(row)
			
		print("list of rows")
		print(list_of_rows)			#DEBUGGING

