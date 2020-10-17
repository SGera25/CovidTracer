


from Person import Person

#Helper method to ensure passed time values are 15 mins long 
def verifyTime(startTime: str, endTime:str):
	if(int(endTime) - int(startTime) != 1459):
		raise AssertionError("entered time block was not 15 mins")

class TimeBlock: 
	#creates an empty set of people and verifies given time 
	def __init__(self, startTime: str, endTime: str):
		self.people = set()
		verifyTime(startTime, endTime)

	def addPerson(self, person: Person):
		self.people.add(person)


	def getRiskSum(self):
		x = 0
		for person in self.people:
			x += person.getRiskValue()
		return x

	def verifyTime(self, startTime: str, endTime:str):
		print(starTime)
		print(endTime)






x = TimeBlock("0", "1459")


