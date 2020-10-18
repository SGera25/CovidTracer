

from collections import deque
import datetime as dt
#Class Location holds a deque containing 14 day objects
from day import Day
from person import Person


class Location:
	
	#On location initialization set address, initialize an dequeue filled with 14 empty days
	def __init__(self, address: str):
		self.address = address
		self.days = deque(maxlen=14)
		self.__fillDeque()

	#override hash function for use in == and !=
	def __hash__(self):
		return hash(self.address)

	#override == for use in comparison in main file
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return hash(self) == hash(other)
		return False
	#override !- for use in comparison in main file
	def __ne__(self, other):
		if isinstance(other, self.__class__):
			return hash(self) != hash(other)
		return False

	def __str__(self):
		return self.address

	#Method used to initialize a deqeue with 14 empty days
	def __fillDeque(self):
		base = dt.date.today()
		for x in range(self.days.maxlen):
			self.days.append(Day(base - dt.timedelta(days = x)))

	#returns a value for a individual's risk value, but also inserts them into the locations Day
	def getRiskValue(self, Date: dt.date, time: tuple, p: Person):
		x = 0
		#iterate over all day objects within the deque
		for day in self.days:
			#compare Dates for equality
			if(Date == day.getDate()):
				#getRiskValue and add that person to all applicable time blocks within the day
				x = day.getRiskValue(time, p)
				day.addPerson(time, p)
		return x 

	#no current functionality but can be useful if we ever need to update days in all locations when we move a day forward
	def updateNewDay(self):
		self.days.pop()
		self.days.appendleft(Day(dt.date.today()))

	def getTotalRiskSum(self):
		x = self.days.popleft()
		self.days.appendleft(x)
		return x.getTotalRiskSum()

