from timeBlock import TimeBlock
from person import Person
import math



class Day:

	#Day Constructor: Initialize an empty list that holds all 94 time blocks for a day
	#each hour has 4 time blocks that are 15 minutes long 
	def __init__(self, Date: str):
		self.initTimeBlocks()


	#Helper method to initialize an empty Day with empty timeBlocks
	def initTimeBlocks(self):
		self.timeBlocks = []
		#Initialize the list to have 96 empty time blocks
		for x in range(96):
			self.timeBlocks.append(TimeBlock())
	#Day method that adds a person to all time blocks they are in;
	#takes time in integers from 0 - 1439 representing 00:00 - 23:59
	def addPerson(self, startTime: int, endTime: int, person: Person):
		#Time blocks time range coorelates to their index i.e. (00:16 is at index 2 because 16/15 is 1)
		#add each person to the time block they were in
		for x in range(math.floor(startTime/15), math.floor(endTime/15) + 1):
			self.timeBlocks[x].addPerson(person)

	#Returns the risk value for a person given start and endtimes by summing the total risk value for
	#that person and all timeblocks they were in
	def getRiskValue(self, startTime: int, enddTime: int, person: Person):
		totalRisk = 0
		for x in range(math.floor(startTime/15), math.floor(endTime/15) + 1):
			totalRisk += self.timeBlocks[x].getRiskSum(person)
		return totalRisk






	




