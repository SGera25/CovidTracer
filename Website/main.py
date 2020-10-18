import math
import datetime as dt

from person import Person
from zip import Zip


class CovidTracer:

	def __init__(self):
		self.zips = {}
		




	#returns the Zip, and Dictionary of locations mapped to their risk value for the past 24 hours
	def getHighRiskLocations(self, zipcode: int):
		return zipcode, self.zips[zipcode].getHighRiskLocations() 


	#returns a risk value for given person and also sets that person within the data structure as well
	#the infoString returns location, time, symptoms, and name
	def getRiskValue(self, name: str, infoString: str):
		entries = infoString.split("###")
		summedRisk = 0
		for entry in entries:
			fields = entry.split("\n")
			risks = ""
			date = 0
			startTime = 0
			endTime = 0
			zipcode = 0
			address = ""
			for x in range(6):
				if x > 2:
					risks += fields[x] + ";"
				elif x == 0:
					date = formatDate(fields[x])
				elif x == 1:
					startTime, endTime = formatTimeRangeIntoInts(fields[x])
				else:
					address, zipcode = getLocationData(fields[x])
			currentPerson = Person(name, risks)
			if zipcode not in self.zips:
				self.zips[zipcode] = Zip(zipcode)
			summedRisk += self.zips[zipcode].getRiskValue(date, (startTime, endTime), address, currentPerson)
		return summedRisk


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
def formatTimeInt(time: str):
	x = time.split(":")
	return (int(x[0]) * 60) + int(x[1])
#Helpe method to formatATime range from ints
def formatTimeRangeIntoInts(timeRange: str):
	x = timeRange.split("-")
	return formatTimeInt(x[0]), formatTimeInt(x[1])
#Gets a date object from a date string
def formatDate(date: str):
	x = date.split("/")
	return dt.date(int(x[2]), int(x[0]), int(x[1]))
#formats zipcode and street address from an address str 
def getLocationData(address: str):
	x = address.split(",")
	return x[0], x[3].replace(" ", "")






if __name__ == '__main__':
	x = CovidTracer()
	#print(x.getRiskValue("billy", "10/18/2020\n00:00 - 00:12\nfake street, draper, UT, 84020\nyes\nfever\n0-5"))
	#print(x.getRiskValue("timmy", "10/18/2020\n00:00 - 00:12\nfake street, draper, UT, 84020\nyes\nCough\n0-5"))
	#print(x.getRiskValue("rudy", "10/18/2020\n00:00 - 00:12\nfake street, draper, UT, 84020\nno\nCough, sore throat\n0-5"))
	#print(x.getRiskValue("jiffy", "10/18/2020\n00:00 - 00:12\nfake street, draper, UT, 84020\nyno\nCough, fever\n0-5"))
	#print(x.getRiskValue("John", "10/18/2020\n00:00 - 00:12\nother location, draper, UT, 84020\nyno\nCongestion\n0-5"))
	#print(x.getHighRiskLocations("84020"))



