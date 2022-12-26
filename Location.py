from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Country(ABC):

    #LIST OF COUNTRIES
    _countryList = []

    @abstractmethod
    def getCountry():
        pass

    def viewCountries(self):
        for x in self._countryList:
            print(x)

class City(ABC):

    #LIST OF CITY
    _cityList = []

    @abstractmethod
    def getCity():
        pass

    def viewCities(self):
        for x in self._cityList:
            print(x)

class Location(Country, City):

    #LIST OF LOCATIONS
    _locationList = []

    def getCountry(self, countryInput):
        countryForPlan = countryInput
        self._countryList.append(countryForPlan)
        return countryForPlan
    
    def getCity(self, cityInput):
        cityForPlan = cityInput
        self._cityList.append(cityForPlan)
        return cityForPlan
    
    def location(self, countryInput, cityInput) -> bool:
        try:
            locationForPlan = self.getCountry(countryInput) + ", " + self.getCity(cityInput)
            self._locationList.append(locationForPlan)
            return True
        except:
            print("UNEXPECTED ERROR")
            return False
        
    def viewLocations(self):
        for x in self._locationList:
            print("Location: " + x)
    
    def locationMenu(self):
        print("Hello and welcome to the Location Menu")
    
        #COUNTRY TEST
        countryInput = input("Enter the Country for your visit: ")
        self.getCountry(countryInput)
        print("THIS IS THE COUNTRY FOR YOUR STAY: ")
        self.viewCountries()

        #CITY TEST
        cityInput = input("Enter the City of that Country for your visit: ")
        self.getCity(cityInput)
        print("THIS IS THE CITY FOR YOUR STAY: ")
        self.viewCities()

        #LOCATION TEST
        self.location(countryInput, cityInput)
        print("THIS IS THE LOCATION FOR YOUR STAY: ")
        self.viewLocations()

if __name__ == "__main__":
    "MAIN METHOD TO TEST THE LOCATION CLASS"

    locationSystem = Location()

    locationSystem.locationMenu()
