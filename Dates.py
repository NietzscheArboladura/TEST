from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import datetime


class Date:

    def getDate(self, yearInput, monthInput, dayInput):
        Ddate = datetime.datetime(yearInput, monthInput, dayInput)
        date = Ddate.date()
        return date

class Departure(Date):
    _departureList = []

    @abstractmethod
    def departureDate(self, yearInput, monthInput, dayInput):
        pass
    
class Return(Date):
    _returnList = []

    @abstractmethod
    def returnDate(self, departureDate, daysOfStay):
        pass

class DatePlan(Departure, Return):

    today = datetime.date.today()
    year = today.year

    def departureDate(self, yearInput, monthInput, dayInput):
        if(yearInput < self.year):
            print("INVALID DATE")
            departuredate = datetime.datetime.now().date()
        else:
            departuredate = self.getDate(yearInput,monthInput,dayInput)
            self._departureList.append(departuredate)
        return departuredate
    
    def returnDate(self, departureDate, daysOfStay):
        returndate = departureDate + datetime.timedelta(days=daysOfStay)
        self._returnList.append(returndate)
        return returndate

    def dateMain(self):
        print("Welcome to the Date menu!")
        print("Our Date currently is: "+ str(datetime.datetime.now().date()))

        departureYear = int(input("Please Enter the Year of your departure: "))
        departureMonth = int(input("Please Enter the Month of your departure: "))
        departureDay = int(input("Please Enter the Day of your departure: "))

        depDate = self.departureDate(departureYear,departureMonth,departureDay)
        self.depDate = depDate
        print("The Date of your Departure will be "+ str(depDate))

        returnDay = int(input("How many days will you be Travelling for: "))
        retDate = self.returnDate(depDate, returnDay)
        self.retDate = retDate
        print("The Date of your Return will be "+ str(retDate))

    depDate = ""
    retDate = ""


if __name__ == "__main__":
    "MAIN METHOD TO TEST THE DATES CLASS"

    dateSystem = DatePlan()

    dateSystem.dateMain()
