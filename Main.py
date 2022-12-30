from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from User import *
from Dates import *
from Destination import *
from Transportation import *
from Budget import *

class TravelPlan(User, DatePlan, Destination, Transportation, MainBudget):

    travelPlanDict = {}

    def viewTravelPlan(self, travelPlanID):
        try:
            if(len(self.travelPlanDict) == 0 or self.travelPlanDict[travelPlanID]["Status"] == False):
                print("Currently no Travel Plan")
            else:
                print("This is Travel Plan ID["+ str(travelPlanID) +"]:")
                print("Travel Plan Name: " + self.travelPlanDict[travelPlanID]["Title"])
                
                try:
                    x = 0
                    for obj in self.travelPlanDict[travelPlanID]["Guests"]:
                        print("Guest ID. #"+ str(x) + " " + obj.fullName)
                        x += 1
                except:
                    print("Unexpected Error")

                print("\nDeparture Date: " + str(self.travelPlanDict[travelPlanID]["Departure Date"]))
                print("\nReturn Date: " + str(self.travelPlanDict[travelPlanID]["Return Date"]))
                print("\nLocation: " + self.travelPlanDict[travelPlanID]["Location"])
                print("\nTransportation ID: " + self.travelPlanDict[travelPlanID]["Transportation ID"])
                print("\nVehicle: " + self.travelPlanDict[travelPlanID]["Vehicle"])
                print("\nPassengers: " + str(self.travelPlanDict[travelPlanID]["Passengers"]))
                print("\nBudget: " + str(self.travelPlanDict[travelPlanID]["Budget"]))
                
        except:
            print("Incomplete Travel Plan!")

    def clearTravelPlan(self):
        try:
            self.travelPlanDict.clear()
            print("Travel Plan Cleared")
        except:
            print("Unexpected Error")
    
    def travelPlanMenu(self, travelPlanID):
        travelPlanChoice = 7
        while travelPlanChoice != 0:
            print("\nManage Travel Plan: "+ self.travelPlanDict[travelPlanID]["Title"])
            print("\n1.) Manage Guests \n2.) Manage Dates \n3.) Manage Location \n4.) Manage Transportation \n5.) Manage Budget \n6.) View Travel Plans\n0.) Return Main Menu")
            travelPlanChoice = int(input("Enter here: "))

            if(travelPlanChoice == 1):
                try:
                    self.userMain()
                except:
                    print("Unexpected Error")
            elif(travelPlanChoice == 2):
                try:
                    self.dateMain()
                    self.travelPlanDict[travelPlanID]["Departure Date"] = self.depDate
                    self.travelPlanDict[travelPlanID]["Return Date"] = self.retDate
                except:
                    print("Unexpected Error")
            elif(travelPlanChoice == 3):
                try:
                    self.destinationMenu()
                    self.travelPlanDict[travelPlanID]["Location"] = self._locationList[travelPlanID]
                except:
                    print("Unexpected Error")
            elif(travelPlanChoice == 4):
                try:
                    self.transportationMenu()
                    self.travelPlanDict[travelPlanID]["Transportation ID"] = self.transpoID
                    self.travelPlanDict[travelPlanID]["Vehicle"] = self.transpoVehicle
                    self.travelPlanDict[travelPlanID]["Passengers"] = self.transpoPassengers
                except:
                    print("Unexpected Error")
            elif(travelPlanChoice == 5):
                try:
                    self.budgetMain()
                    self.travelPlanDict[travelPlanID]["Budget"] = self.TotalBudget
                except:
                    print("Unexpected Error")
            elif(travelPlanChoice == 6):
                try:
                    self.viewTravelPlan(travelPlanID)
                except:
                    print("Unexpected Error")

    
    def viewTitles(self):
        print("Current Travel Plans")
        for x in range(len(self.travelPlanDict)):
            if(self.travelPlanDict[x]["Status"] == True):
                print("Travel Plan ID["+ str(x) +"]: "+ self.travelPlanDict[x]["Title"])

    def removeTravelPlan(self, travelplanID):
        try:
            self.travelPlanDict.pop(travelplanID)
            print("Travel Plan Removed")
        except:
            print("Unexpected Error")
    
    def softDeleteTravelPlan(self, travelplanID):
        try:
            self.travelPlanDict[travelplanID]["Status"] = False
            print("Travel Plan Removed")
        except:
            print("Unexpected Error")
    
    def travelPlanMain(self):
        numberOfTravelPlans = int(input("***Welcome Visitors!***\nHow many Travel Plans are you going to make today: "))

        try:
            for x in range(numberOfTravelPlans):
                self.travelPlanDict[x] = {}

                travelPlanName = input("Input the Name for Travel Plan ID["+ str(x) +"]: ")
                self.travelPlanDict[x]["Title"] = travelPlanName
                self.travelPlanDict[x]["Status"] = True
                print("Currently no people on the trip, add some!")
                self.travelPlanDict[x]["Guests"] = self.addUser()

            travelPlanMain = 5
            while travelPlanMain > 0:
                print("***Travel Plan Main Menu***")
                print("\n1.) Manage a Travel Plan \n2.) View Travel Plans \n3.) Remove a Travel Plan \n0.) EXIT APPLICATION")
                travelPlanMain = int(input("Enter here: "))

                if(travelPlanMain == 1):
                    self.viewTitles()
                    tpChoice = int(input("Enter the Travel Plan ID here: "))
                    self.travelPlanMenu(tpChoice)
                    self.viewTravelPlan(tpChoice)
                elif(travelPlanMain == 2):
                    try:
                        self.viewTitles()
                        tpChoice = int(input("Enter the Travel Plan ID here: "))
                        self.viewTravelPlan(tpChoice)
                    except:
                        print("Unexpected Error in Viewing Travel Plan")
                elif(travelPlanMain == 3):
                    try:
                        self.viewTitles()
                        tpChoice = int(input("Enter the Travel Plan ID here: "))
                        self.softDeleteTravelPlan(tpChoice)
                    except:
                        print("Unexpected Error")
            else:
                print("Thank You and Come Again!")
                print(exit)

        except:
            print("Unexpected Error")

        


if __name__ == "__main__":
    "MAIN METHOD"
    travelPlanSystem = TravelPlan()

    travelPlanSystem.travelPlanMain()
