


from person import Person


class TimeBlock: 
	#creates an empty set of people and verifies given time 
	def __init__(self):
		self.people = set()

	def addPerson(self, person: Person):
		self.people.add(person)


	#iterates over all the people within a timeblock at a location and sums their riskValue 
	def getRiskSum(self, person: Person):
		x = 0

		for y in self.people:
			#ignore self
			if(person != y):
				x += y.getRiskValue()
		return x


