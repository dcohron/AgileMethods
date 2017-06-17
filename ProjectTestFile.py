#  Class: SSW-555
#  Project:  GEDCOM Project Test Repository
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 13 June 2017

# Testing Project Increments

# Honor Code Statement
# W pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll            Date: 7 June 2017
# Signature: Amie Widerkehr         Date: 7 June 2017
# Signature: David N. Cohron        Date: 7 June 2017

# References:
# 1) StackOverflow
# 2) PyUnit Tutorial: "Page." PyUnit - Python Wiki. N.p., n.d. Web. 13 June 2017.

import unittest
from Sprint1 import *

class AgileProjectTests(unittest.TestCase):

    def setUp(self):
        # Call before every test case.
        # self.checkdates = checkDates()
        
        self.date1 = ("10MAR1960")
        self.date2 = ("10MAR1970")
        self.emptyDate = "NA"

        # set_verbose

    def tearDown(self):
        # Call after every test case.
        print("Test complete.")

    def testCompareDate(self):
        # Test case to check date comparison.
         assert checkDates(self.date1, self.date2) == True, "Dates do not check."
	
    def testReverseCompareDate(self):
        # Test case to check date comparison of reversed.
        assert checkDates(self.date2, self.date1) == False, "Reverse dates do not check."

    def testSameDate(self):
        # Test case to check date comparison of same dates.
        assert checkDates(self.date1, self.date1) == False, "Same dates do not check."    

    def testOffset1(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date2, 35598) == False, "Offset1 incorrect."

    def testOffset2(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date2, 10) == True, "Offset2 incorrect."

    def testOffset3(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date1, -36000) == True, "Offset3 incorrect."

    def testUS04_CheckDivorceAfterMarriage(self):
        print()
        
        # Successful Path: Will be successful:
        print("Testing US04_checkMarriageBeforeDivorce Check:")

        assert marriageBeforeDivorce(self.date1, self.date2) == True, "Marriage: " + self.date1 + " Divorce: " + self.date2        

        # Negative Test Case: Will Fail:
        #print("Testing US04_checkMarriageBeforeDivorce Negative Test Case:")
        #assert marriageBeforeDivorce(self.date2, self.date1) == True, "Marriage: " + self.date2 + " Divorce: " + self.date1

    def testUS05_CheckDeathAfterMarriage(self):
        print()

         # Successful Path: Will be successful:
        print("Testing US05_marriageBeforeDeathCheck:")

        assert marriageBeforeDeathCheck("F1", self.date1, self.date2, self.date2) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.date2
    
        assert marriageBeforeDeathCheck("F1", self.date1, self.date2, self.emptyDate) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.emptyDate

        assert marriageBeforeDeathCheck("F1", self.date1, self.emptyDate, self.date2) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date2

        assert marriageBeforeDeathCheck("F1", self.date1, self.emptyDate, self.emptyDate) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.emptyDate
        
        # Negative Test Case: Will Fail
        
        #print("Testing US05_marriageBeforeDeathCheck Negative Test Case:")

        #assert marriageBeforeDeathCheck("F1", self.date2, self.date1, self.date2) == True, "F1: " + "Marriage: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.date2
    
        #assert marriageBeforeDeathCheck("F1", self.date2, self.date1, self.emptyDate) == True, "F1: " + "Marriage: " + self.date2+ " Husband Death: " + self.date1 + " Wife Death: " + self.emptyDate

        #assert marriageBeforeDeathCheck("F1", self.date2, self.emptyDate, self.date1) == True, "F1: " + "Marriage: " + self.date2 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date1


if __name__ == "__main__":

	# run all tests
    unittest.main() 

# End of File
