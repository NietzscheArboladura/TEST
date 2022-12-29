from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Person(object):
    "Person Object"
    def __init__(self, fullname, age, gender):
        self.fullName = fullname
        self.age = age
        self.gender = gender


class Guest:

    _guestList = []

    listLength = 0

    def addGuest(self):
        gList = []
        print("Hello this is where you will be adding the Guests")
        numberOfGuests = int(input("Enter the number of people joining the Travel Plan: "))
        print("There are is a total of: "+ str(numberOfGuests) + " guests.")

        for x in range(numberOfGuests):
            guestName = input("Enter the name of the Guest no."+ str(x + 1) + ": ")
            guestAge = int(input("Enter the Guest's age: "))
            guestGender = input("Enter the Guest gender [Male/Female/Other]: ")
            self._guestList.append(Person(guestName,guestAge,guestGender))
            gList.append(Person(guestName,guestAge,guestGender))

            self.listLength = len(gList)
            print()
        
        return gList
    
    
    def removeGuest(self):
        try:
            print("Remove a Guest -  \nPlease Select the Guest among the list below - ")
            x = 0
            for obj in guestSystem._guestList:
                print("Index no."+ str(x) + " " + obj.fullName)
                x += 1
            guestToRemove = int(input("Enter the Index number of the Guest you want to Remove: "))
            self._guestList.pop(guestToRemove)
        except:
            print("Unexpected Error")
        
    def showGuestList(self):
        if(len(self._guestList) > 0):
            print("Current Guests:")
            x = 0
            for obj in self._guestList:
                print("Guest ID."+ str(x) + " " + obj.fullName)
                x += 1
        else:
            print("There are Currently no Guests")
    
    def guestMain(self):
        print("Welcome to the Companions Menu!")
        if(len(self._guestList) == 0):
            print("There are Currently no people going on the trip, time to add some people.")
            self.addGuest()
            self.showGuestList()
        else:
            print("There are Currently " + str(self.listLength) + " guests")
            gChoice = int(input("What would you like to do? 1.) Add more Guests 2.) Remove a Guest \nEnter Choice Here: "))
            if(gChoice == 1):
                self.addGuest()
            else:
                self.removeGuest()
        

if __name__ == "__main__":
    "MAIN METHOD TO TEST THE GUEST CLASS"
    guestSystem = Guest()

    guestSystem.guestMain()

        

