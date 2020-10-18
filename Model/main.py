import math, Model, datetime
from openpyxl import load_workbook
class CovidTracer:

	def __init__(self):
		self.zips = {}
		




	#returns the Zip, and Dictionary of locations mapped to their risk value for the past 24 hours
	def getHighRiskLocations(self, zipcode: int):
		return zipcode, self.zips[zipcode].getHighRiskLocations() 


	#returns a risk value for given person and also sets that person within the data structure as well
	#the infoString returns location, time, symptoms, and name
	def getRiskValue(self, infoString: str):
		self.zips
		return 1
		



#helper method returns a str formatted as a time range within 00:00-23:59 
def formatTimeRange(startTime: int, endTime: int):
	startHours = str(math.floor(startTime/60))
	startMins = str(math.floor(startTime % 60))
	endHours = str(math.floor(endTime/60))
	endMins = str(math.floor(endTime % 60))
	if len(startHours) < 2:
		startHours = "0" + startHours
	if len(startMins) < 2:
		startMins = "0" + startMins
	if len(endHours) < 2:
		endHours = "0" + endHours
	if len(endMins) < 2:
		endMins = "0" + endMins

	return startHours + ":" + startMins + " - " + endHours + ":" + endMins
#helper method that returns two ints based on the given time range 
def formatTimeInt(timeRange: str):
	x = timeRange.split(":")
	return (int(x[0]) * 60) + int(x[1])







