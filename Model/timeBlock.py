


from person import Person


class TimeBlock: 
	#creates an empty set of people and verifies given time 
	def __init__(self):
		self.people = {}

	def addPerson(self, person: Person):
		self.people[person.getName] = person


	#iterates over all the people within a timeblock at a location and sums their riskValue 
	def getRiskSum(self, person: Person):
		x = 0

		for y in self.people:
			#ignore self
			if(person.getName() != y):
				x += self.people[y].getRiskValue()
		return x

	def getTotalRiskSum(self):
		x = 0
		for y in self.people:
			x += self.people[y].getRiskValue()
		return x


