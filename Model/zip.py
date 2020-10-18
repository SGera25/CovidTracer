
from location import Location
from person import Person
import datetime as dt

class Zip:

	def __init__(self, zipcode: int):
		self.zipcode = zipcode
		self.locations = {}
		assert (self.zipcode < 1000000 and self.zipcode > 0)

	def getZip(self):
		return self.zipcode

	def getRiskValue(self, Date: dt.date, time: tuple, location: str, person: Person):
		if(location not in self.locations):
			self.locations[location] = Location(location)
		return self.locations[location].getRiskValue(Date, time, person)

	def getHighRiskLocations(self):
		locMappedValues = {}
		for y in self.locations:
			locMappedValues[y] = self.locations[y].getTotalRiskSum()
		return locMappedValues



p = Person("john", "risks")
o = Person("bill", "risks")
x = Zip(34685)
x.getRiskValue(dt.date.today, (0,16), "14247 S canyon vine cove", p)
x.getRiskValue(dt.date.today, (0,16), "14247 S canyon vine cove", o)
print(x.locations)