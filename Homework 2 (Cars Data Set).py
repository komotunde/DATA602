
#1. fill in this class
#   it will need to provide for what happens below in the
#	main, so you will at least need a constructor that takes the values as (Brand, Price, Safety Rating),
# 	a function called showEvaluation, and an attribute carCount
class CarEvaluation:
	"""A simple class that represents a car evaluation"""
	#all your logic here

        carCount = 0

        def __init__(self, Brand, Price, SafetyRating):
            self.Brand = Brand
            self.Price = Price
            self.SafetyRating = SafetyRating
            CarEvaluation.carCount += 1

        def showEvaluation(self):
            """Shows the attributes of the object"""
            print "The", self.Brand, "has a ", self.Price, "price", "and it's safety is rated a", self.SafetyRating

        def __repr__(self):
            return self.Brand
#My output for teh  order function was not correct until I added the above code. It displays characteristics of the item.

#2. fill in this function
#   it takes a list of CarEvaluation objects for input and either "asc" or "des"
#   if it gets "asc" return a list of car names order by ascending price
# 	otherwise by descending price
#  you fill in the rest

        def sortbyprice(List, Rank):
            SortedList = []
            for i in List:
                if i.Price == "Low":
                    SortedList.append(i.Brand)
                elif i.Price == "Med":
			         SortedList.append(i.Brand)
                else:
			         SortedList.append(i.Brand)
            if Rank == "asc":
		      return SortedList.reverse()


#3. fill in this function
#   it takes a list for input of CarEvaluation objects and a value to search for
#	it returns true if the value is in the safety  attribute of an entry on the list,
#   otherwise false
#   you fill in the rest

        def searchforsafety(List, Value):
            """Takes a list of CarEvaluation objects and value to search for. It returns true if the value is in the safety attribute of an entry on the list, otherwise, false."""
            for car in List:

                if car.SafetyRating == Value:

                    return True
            else:

                    return False


# This is the main of the program.  Expected outputs are in comments after the function calls.
if __name__ == "__main__":
   eval1 = CarEvaluation("Ford", "High", 2)
   eval2 = CarEvaluation("GMC", "Med", 4)
   eval3 = CarEvaluation("Toyota", "Low", 3)

   print "Car Count = %d" % CarEvaluation.carCount # Car Count = 3

   eval1.showEvaluation() #The Ford has a High price and it's safety is rated a 2
   eval2.showEvaluation() #The GMC has a Med price and it's safety is rated a 4
   eval3.showEvaluation() #The Toyota has a Low price and it's safety is rated a 3

   L = [eval1, eval2, eval3]

   print sortbyprice(L, "asc"); #[Toyota, GMC, Ford]
   print sortbyprice(L, "des"); #[Ford, GMC, Toyota]
   print searchforsafety(L, 2); #true
   print searchforsafety(L, 1); #false

#Note, I spent about 30 minutes trying to figure out why I kept getting a "this construct does not take any inputs" only to discover it was a typo. After correcting a few mistakes, I have ended here where when ran, by functions give an error of not defined when in fact, they are.