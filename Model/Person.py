



class Person:
	#constructor that initializes a person's name and their relevant risk factors

	def __init__(self, name: str, riskFactorString: str):
		self.name = name
		self.initRiskFactors(riskFactorString)
		self.riskValue = 0



	#helper method that calculates the riskValue for a person given their riskFactorstring
	def initRiskFactorValue(self, riskFactors: str):
		return 1

#Overrided Obj !=, ==, and hash functions to make comparison of person objects appropriate
	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		if isinstance(self, other):
			return hash(self) == hash(other)

	def __ne__(self, other):
		if isinstance(self, other):
			return hash(self) != hash(other)

	#getter for riskValue
	def getRiskValue(self):
		return self.riskValue



		