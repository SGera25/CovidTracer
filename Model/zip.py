
import datetime as dt

from Model.location import Location
from Model.person import Person


class Zip:

	def __init__(self, zipcode: int):
		self.zipcode = int(zipcode)
		self.locations = {}
		assert (1000000 > self.zipcode > 0)

	def getZip(self):
		return self.zipcode

	def getRiskValue(self, Date: dt.date, time: tuple, location: str, person: Person):
		if location not in self.locations:
			self.locations[location] = Location(location)
		return self.locations[location].getRiskValue(Date, time, person)

	def getHighRiskLocations(self):
		locMappedValues = {}
		for y in self.locations:
			locMappedValues[y] = self.locations[y].getTotalRiskSum()
		return locMappedValues

