



class Person:
	
	def __init__(self, name: str, riskFactorString: str):
		self.name = name
		self.initRiskFactors(riskFactorString)




	def initRiskFactors(self, riskFactors: str):
		self.riskFactors = {}



	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		if isinstance(self, other):
			return self.name == self.name

	def getRiskValue(self):
		return 1



		