
from location import Location
from person import Person
import datetime as dt

class Zip:

	def __init__(self, zipcode: int):
		self.zipcode = zipcode
		self.locations = {}

	def getRiskValue(self, Date: dt.date, time: tuple, location: str, person: Person):
		if(not self.locations.has_key(location)):
			self.locations[location] = Location(location)
		return self.locations[location].getRiskValue(Date, time, person)