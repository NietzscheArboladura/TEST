from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class AbstractTranspo(ABC):

    @abstractmethod
    def getTranspo():
        pass
    def changeTranspoPassengers():
        pass
    def removeTranspo():
        pass

class landTransportation():

    landTranspoDict = {
        "LV01" : {
            "Vehicle": "Car",
            "Passengers": 4
        },
        "LV02" : {
            "Vehicle": "Van",
            "Passengers": 8
        },
        "LV03" : {
            "Vehicle": "Truck",
            "Passengers": 15
        },
    }

    def viewLandDictionary(self):
        print("\nAvailable Land transportations:")
        for key, value in self.landTranspoDict.items():
            print(key, " : " , value)
        return self.landTranspoDict


class seaTransportation():

    seaTranspoDict = {
        "SV01" : {
            "Vehicle": "Motorboat",
            "Passengers": 8
        },
        "SV02" : {
            "Vehicle": "Sailboat",
            "Passengers": 15
        },
        "SV03" : {
            "Vehicle": "Cruise Ship",
            "Passengers": 100
        },
    }

    def viewSeaDictionary(self):
        print("\nAvailable Sea transportations:")
        for key, value in self.seaTranspoDict.items():
            print(key, " : " , value)
        return self.seaTranspoDict

class airTransportation():

    airTranspoDict = {
        "AV01" : {
            "Vehicle": "Helicopter",
            "Passengers": 6
        },
        "AV02" : {
            "Vehicle": "Private Jet",
            "Passengers": 20
        },
        "AV03" : {
            "Vehicle": "Passenger Airline",
            "Passengers": 100
        },
    }

    def viewAirDictionary(self):
        print("\nAvailable Air transportations:")
        for key, value in self.airTranspoDict.items():
            print(key, " : " , value)
        return self.airTranspoDict

class Transportation(AbstractTranspo, landTransportation, seaTransportation, airTransportation):
    
    transpoID = ""
    transpoVehicle = ""
    transpoPassengers = ""

    def getTranspo(self, transpoInfo, transpoID):

        try:
            if(transpoInfo[transpoID] != None):
                self.transpoID = transpoID
                self.transpoVehicle = transpoInfo[transpoID]['Vehicle']
                self.transpoPassengers = transpoInfo[transpoID]['Passengers']
                print("Transport ID: " + str(transpoID))
                print("Vehicle: ", transpoInfo[transpoID]['Vehicle'])
                print("Passengers: ", transpoInfo[transpoID]['Passengers'])
        except:
            print("Transportation does not Exist!")
    
    def changeTranspoPassengers(self, transpoInfo, transpoID, numOfPassengers):

        try:
            transpoInfo[transpoID]['Passengers'] = numOfPassengers
            print("The Number of Passengers has been changed into: " + str(numOfPassengers))
        except:
            print("Unexpected Error")
    
    def removeTranspo(self, transpoInfo, ltID):

        try:
            transpoInfo.pop(ltID)
            print("The Transportation of TransportID " + str(ltID) + " has been Deleted")
        except:
            print("Unexpected Error")
    
    def viewDictionaries(self):
        print("Transportation Dictionaries:")
        print("Available Land transportations:")
        for key, value in self.landTranspoDict.items():
            print(key, " : " , value)
        print("Available Sea transportations:")
        for key, value in self.seaTranspoDict.items():
            print(key, " : " , value)
        print("Available Air transportations:")
        for key, value in self.airTranspoDict.items():
            print(key, " : " , value)
    
    def transportationMenu(self):
        print("Hello and welcome to the Transportation Test Method")
        self.viewDictionaries()

        print("***Transportation Menu***\n1.) Select mode of Transportation\n2.) Change Number of Passengers\n3.) Remove Mode of Transport\n0.) EXIT")
        transpoChoice = int(input("Enter Choice Here: "))

        if(transpoChoice == 1):
            transpoInfo = input("Available Modes of Transportations: [Land, Sea, Air] \nWhich would you like to utilize: ") 

            if(transpoInfo == "Land" or transpoInfo == "land"):
                transpoDict = self.viewLandDictionary()
            elif(transpoInfo == "Sea" or transpoInfo == "sea"):
                transpoDict = self.viewSeaDictionary()
            elif(transpoInfo == "Air" or transpoInfo == "air"):
                transpoDict = self.viewAirDictionary()

            transpoID = input("Input Transportation ID here: ")
            self.getTranspo(transpoDict, transpoID)

        elif(transpoChoice == 2):
            print("Here, you can change the number of Passengers")
            transpoMode = input("Select a Mode of Transportation: [Land, Sea, Air] ")
            if(transpoMode == "Land" or transpoMode == "land"):
                transpoInfo = self.viewLandDictionary()
            elif(transpoMode == "Sea" or transpoMode == "sea"):
                transpoInfo = self.viewSeaDictionary()
            elif(transpoMode == "Air" or transpoMode == "air"):
                transpoInfo = self.viewAirDictionary()
            transpoID = input("Input Transportation ID here: ")
            transpoPass = int(input("How many Passengers to change: "))
            self.changeTranspoPassengers(transpoInfo,transpoID,transpoPass)
                
            print("The Updated Transport Info:")
            transpoSystem.getTranspo(transpoInfo, transpoID)

        elif(transpoChoice == 3):
            transpoInfo = input("Available Modes of Transportations: [Land, Sea, Air] \nWhich would you like to remove: ")

            if(transpoInfo == "Land" or transpoInfo == "land"):
                    transpoDict = self.viewLandDictionary()
            elif(transpoInfo == "Sea" or transpoInfo == "sea"):
                    transpoDict = self.viewSeaDictionary()
            elif(transpoInfo == "Air" or transpoInfo == "air"):
                    transpoDict = self.viewAirDictionary()

            transpoID = input("Input their Transportation ID here: ")
            self.removeTranspo(transpoDict, transpoID)

     
if __name__ == "__main__":
    "MAIN METHOD TO TEST THE TRANSPORTATION CLASS"

    transpoSystem = Transportation()

    transpoSystem.transportationMenu()

    
