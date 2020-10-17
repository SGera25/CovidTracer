


from Person import Person


class TimeBlock: 
	#creates an empty set of people and verifies given time 
	def __init__(self):
		self.people = set()
		print("made timeBlock")

	def addPerson(self, person: Person):
		self.people.add(person)



	def getRiskSum(self):
		x = 0
		for person in self.people:
			x += person.getRiskValue()
		return x


