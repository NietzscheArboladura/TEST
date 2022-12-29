from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from Guest import *
from Dates import *
from Location import *
from Transportation import *
from Budget import *

class TravelPlan(Guest, DatePlan, Location, Transportation, MainBudget):

    travelPlanDict = {}

    def viewTravelPlan(self, travelPlanID):
        try:
            if(len(self.travelPlanDict) == 0 or self.travelPlanDict[travelPlanID]["Status"] == False):
                print("There is Currently no Travel Plan")
            else:
                print("Well Done! This is Travel Plan ID["+ str(travelPlanID) +"]:")
                print("Travel Plan Title: " + self.travelPlanDict[travelPlanID]["Title"])
                
                try:
                    x = 0
                    for obj in self.travelPlanDict[travelPlanID]["Guests"]:
                        print("Guest ID."+ str(x) + " " + obj.fullName)
                        x += 1
                except:
                    print("Unexpected Error in showing guests")

                print("Departure Date: " + str(self.travelPlanDict[travelPlanID]["Departure Date"]))
                print("Return Date: " + str(self.travelPlanDict[travelPlanID]["Return Date"]))
                print("Location: " + self.travelPlanDict[travelPlanID]["Location"])
                print("Transportation ID: " + self.travelPlanDict[travelPlanID]["Transportation ID"])
                print("Vehicle: " + self.travelPlanDict[travelPlanID]["Vehicle"])
                print("Passengers: " + str(self.travelPlanDict[travelPlanID]["Passengers"]))
                print("Budget: " + str(self.travelPlanDict[travelPlanID]["Budget"]))
                
        except:
            print("Travel Plan Incomplete!")

    def clearTravelPlan(self):
        try:
            self.travelPlanDict.clear()
            print("The Travel Plan has been Cleared")
        except:
            print("Unexpected Error, Travel Plan has not been Cleared")
    
    def travelPlanMenu(self, travelPlanID):
        travelPlanChoice = 7
        while travelPlanChoice != 0:
            print("Manage Travel Plan: "+ self.travelPlanDict[travelPlanID]["Title"])
            print("What would you like to do? \n1.) Manage Guests \n2.) Manage Dates \n3.) Manage Location \n4.) Manage Transportation \n5.) Manage Budget \n6.) View Current Travel Plan \n0.) Return to Main Menu")
            travelPlanChoice = int(input("Enter your choice here: "))

            if(travelPlanChoice == 1):
                try:
                    self.guestMain()
                except:
                    print("Unexpected Error in Managing Guests")
            elif(travelPlanChoice == 2):
                try:
                    self.dateMain()
                    self.travelPlanDict[travelPlanID]["Departure Date"] = self.depDate
                    self.travelPlanDict[travelPlanID]["Return Date"] = self.retDate
                except:
                    print("Unexpected Error in Managing Dates")
            elif(travelPlanChoice == 3):
                try:
                    self.locationMenu()
                    self.travelPlanDict[travelPlanID]["Location"] = self._locationList[travelPlanID]
                except:
                    print("Unexpected Error in Managing Location")
            elif(travelPlanChoice == 4):
                try:
                    self.transportationMenu()
                    self.travelPlanDict[travelPlanID]["Transportation ID"] = self.transpoID
                    self.travelPlanDict[travelPlanID]["Vehicle"] = self.transpoVehicle
                    self.travelPlanDict[travelPlanID]["Passengers"] = self.transpoPassengers
                except:
                    print("Unexpected Error in Managing Transportation")
            elif(travelPlanChoice == 5):
                try:
                    self.budgetMain()
                    self.travelPlanDict[travelPlanID]["Budget"] = self.TotalBudget
                except:
                    print("Unexpected Error in Managing Budget")
            elif(travelPlanChoice == 6):
                try:
                    self.viewTravelPlan(travelPlanID)
                except:
                    print("Unexpected Error in Managing Budget")

    
    def viewTitles(self):
        print("Current Travel Plans")
        for x in range(len(self.travelPlanDict)):
            if(self.travelPlanDict[x]["Status"] == True):
                print("Travel Plan ID["+ str(x) +"]: "+ self.travelPlanDict[x]["Title"])

    def removeTravelPlan(self, travelplanID):
        try:
            self.travelPlanDict.pop(travelplanID)
            print("The Travel Plan has been Removed")
        except:
            print("Unexpected Error, Travel Plan has not been Removed")
    
    def softDeleteTravelPlan(self, travelplanID):
        try:
            self.travelPlanDict[travelplanID]["Status"] = False
            print("The Travel Plan has been Removed")
        except:
            print("Unexpected Error, Travel Plan has not been Removed")
    
    def travelPlanMain(self):
        numberOfTravelPlans = int(input("Hello! \nSo how many Travel Plans are you going to make today: "))

        try:
            print("Welcome! Time to Create a Travel Plan!")
            for x in range(numberOfTravelPlans):
                self.travelPlanDict[x] = {}

                travelPlanName = input("Input the Title for Travel Plan ID["+ str(x) +"]: ")
                self.travelPlanDict[x]["Title"] = travelPlanName
                self.travelPlanDict[x]["Status"] = True
                print("There are Currently no people going on the trip, time to add some people.")
                self.travelPlanDict[x]["Guests"] = self.addGuest()

            travelPlanMain = 5
            while travelPlanMain > 0:
                print("This is the Travel Plan Main Menu")
                print("What would you like to do? \n1.) Manage a Travel Plan \n2.) View Travel Plans \n3.) Remove a Travel Plan \n0.) EXIT APPLICATION")
                travelPlanMain = int(input("Enter your choice here: "))

                if(travelPlanMain == 1):
                    print("Select a Travel Plan to Manage:")
                    self.viewTitles()
                    tpChoice = int(input("Enter the Travel Plan ID here: "))
                    self.travelPlanMenu(tpChoice)
                    self.viewTravelPlan(tpChoice)
                elif(travelPlanMain == 2):
                    try:
                        print("Select a Travel Plan to View:")
                        self.viewTitles()
                        tpChoice = int(input("Enter the Travel Plan ID here: "))
                        self.viewTravelPlan(tpChoice)
                    except:
                        print("Unexpected Error in Viewing Travel Plan")
                elif(travelPlanMain == 3):
                    try:
                        print("Select a Travel Plan to Remove:")
                        self.viewTitles()
                        tpChoice = int(input("Enter the Travel Plan ID here: "))
                        self.softDeleteTravelPlan(tpChoice)
                    except:
                        print("Unexpected Error in clearing Travel Plan")
            else:
                print("Thank you!")
                print(exit)

        except:
            print("Unexpected Error in creating Travel Plan")

        


if __name__ == "__main__":
    "MAIN METHOD"
    travelPlanSystem = TravelPlan()

    travelPlanSystem.travelPlanMain()
