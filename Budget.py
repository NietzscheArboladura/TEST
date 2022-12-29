from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Budget(ABC):

    _budgetList = []


    @staticmethod
    @abstractmethod

    def budget_size():
        pass

class TripBudget(Budget):
    
    def budget_size(self,budget_input):
        self._budgetList.append(budget_input)
        return "Current Budget Size: " + str(budget_input)


class EmergencyBudget(Budget):
        
    def budget_size(self,budget_input):
        self._budgetList.append(budget_input)
        return "Emergency Budget Size: " + str(budget_input)


class ConversionBudget(Budget):
        
    def budget_size(self,budget_input,conversion_rate):
        self._budgetList.clear()
        budget_input = budget_input/conversion_rate
        self._budgetList.append(budget_input)
        return "Conversion Budget Size: " + str(budget_input)

class MainBudget(TripBudget, EmergencyBudget, ConversionBudget):
    
    TotalBudget = 0

    def budgetMain(self):
        
        tripBudgetSystem = TripBudget()
        emergencyBudgetSystem = EmergencyBudget()
        ConversionBudgetSystem = ConversionBudget()

        print("Welcome to the Budget Menu!")
        print("Let's first input the current Trip Budget:")
        tripBudget = int(input("Enter the Current Budget for the trip: "))
        tripBudgetSystem.budget_size(tripBudget)

        print("Next let's input the Emergency Budget: ")
        emergencyBudget = int(input("Enter the Emergency Budget for the trip: "))
        emergencyBudgetSystem.budget_size(emergencyBudget)

        print("Are you planning to go on a Foreign Country?")
        ans = input("[Yes/y or No/n]: ")

        if (ans == "Yes" or ans == "y"):
            preBudget = sum(self._budgetList)
            print("This is your current Budget: " + str(preBudget))
            converRate = float(input("Enter the Conversion Rate of that Country to yours: "))
            ConversionBudgetSystem.budget_size(preBudget,converRate)
            totalBudget = sum(self._budgetList)
            self.TotalBudget = round(totalBudget,2)
            print("Your Total Budget for that Country is " + str(round(totalBudget, 2)))
        else:
            totalBudget = sum(self._budgetList)
            self.TotalBudget = totalBudget
            print("Your Total Budget is " + str(totalBudget))




if __name__ == "__main__":
    "MAIN METHOD TO TEST THE BUDGET CLASS"

    budgetSystem = MainBudget()

    budgetSystem.budgetMain()

    