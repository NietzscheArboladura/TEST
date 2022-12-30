from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Country(ABC):

    _countryList = []

    @abstractmethod
    def getCountry():
        pass

    def viewCountries(self):
        for x in self._countryList:
            print(x)

class City(ABC):

    _cityList = []

    @abstractmethod
    def getCity():
        pass

    def viewCities(self):
        for x in self._cityList:
            print(x)

class Location(Country, City):

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
        print("***Location Menu***")
    
        countryInput = input("Country you want to visit: ")
        self.getCountry(countryInput)
        print("This is the country you'll be staying: ")
        self.viewCountries()

        cityInput = input("City of that Country you want to visit: ")
        self.getCity(cityInput)
        print("This is the city you'll be staying: ")
        self.viewCities()

        self.location(countryInput, cityInput)
        print("This is the location of you visit: ")
        self.viewLocations()

if __name__ == "__main__":
    "MAIN METHOD TO TEST THE LOCATION CLASS"

    locationSystem = Location()

    locationSystem.locationMenu()
