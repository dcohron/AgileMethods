#  Class: SSW-555
#  Project:  GEDCOM Project Test Repository
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 27 June 2017

# Testing Project Increments

# Honor Code Statement
# W pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll            Date: 27 June 2017
# Signature: Amie Widerkehr         Date: 27 June 2017
# Signature: David N. Cohron        Date: 27 June 2017

# References:
# 1) StackOverflow
# 2) PyUnit Tutorial: "Page." PyUnit - Python Wiki. N.p., n.d. Web. 13 June 2017.

import unittest
from Sprint2 import *

class AgileProjectTests(unittest.TestCase):

    def setUp(self):
        # Call before every test case.
        # self.checkdates = checkDates()
        
        self.date1 = ("10MAR1960")
        self.date2 = ("10MAR1970")
        self.emptyDate = "NA"

        self.date3 = ("10MAR1889")
        self.date4 = ("10MAR1899")
        self.date5 = ("10MAR1920")
        
        self.individualsTest = {'I1': {'NAME': 'Mike/Brady/', 'SEX': 'M', 'BIRT': '10MAR1940', 'DEAT': 'NA'}, 'I2': {'NAME': 'Carol/Martin/', 'SEX': 'F', 'BIRT': '10MAR1945', 'DEAT': 'NA'}, 'I3': {'NAME': 'Sam/Franklin/', 'SEX': 'M', 'BIRT': '10MAR1930', 'DEAT': 'NA'}, 'I4': {'NAME': 'Alice/Nelson/', 'SEX': 'F', 'BIRT': '10MAR1925', 'DEAT': 'NA'}, 'I5': {'NAME': 'Greg/Brady/', 'SEX': 'M', 'BIRT': '10MAR1955', 'DEAT': 'NA'}, 'I6': {'NAME': 'Peter/Brady/', 'SEX': 'M', 'BIRT': '10MAR1950', 'DEAT': 'NA'}, 'I7': {'NAME': 'Bobby/Brady/', 'SEX': 'M', 'BIRT': '10MAR1960', 'DEAT': 'NA'}, 'I8': {'NAME': 'Marcia/Nelson/', 'SEX': 'F', 'BIRT': '10MAR1956', 'DEAT': 'NA'}, 'I9': {'NAME': 'Jan/Nelson/', 'SEX': 'F', 'BIRT': '10MAR1958', 'DEAT': 'NA'}, 'I10': {'NAME': 'Cindy/Nelson/', 'SEX': 'F', 'BIRT': '10MAR1960', 'DEAT': 'NA'}, 'I11': {'NAME': 'Tiger/Brady/', 'SEX': 'M', 'BIRT': '10MAR1965', 'DEAT': 'NA'}, 'I12': {'NAME': 'Sally/Fields/', 'SEX': 'F', 'BIRT': '10MAR1942', 'DEAT': '10MAR1940'}, 'I13': {'NAME': 'Samuel/Jackson/', 'SEX': 'M', 'BIRT': '10MAR1979', 'DEAT': 'NA'}, 'I14': {'NAME': 'Natashia/Richards/', 'SEX': 'F', 'BIRT': '30MAR1981', 'DEAT': '10MAR2012'}, 'I15': {'NAME': 'Benjamin/Franklin/', 'SEX': 'M', 'BIRT': '17JAN1706', 'DEAT': '17APR1790'}, 'I16': {'NAME': 'Deborah/Reed/', 'SEX': 'F', 'BIRT': '10MAR1800', 'DEAT': '10MAR1880'}, 'I17': {'NAME': 'Homestar/Franklin/', 'SEX': 'M', 'BIRT': '10MAR1990', 'DEAT': 'NA'}}
        self.familiesTest = {'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': [], 'MARR': '10MAR1970', 'DIV': 'NA'}, 'F2': {'HUSB': 'I1', 'WIFE': 'I12', 'CHIL': [], 'MARR': '10MAR1969', 'DIV': 'NA'}, 'F3': {'HUSB': 'I3', 'WIFE': 'I4', 'CHIL': ['I2'], 'MARR': '10MAR1928', 'DIV': 'NA'}, 'F4': {'HUSB': 'I15', 'WIFE': 'I16', 'CHIL': ['I3', 'I17'], 'MARR': '10MAR1990', 'DIV': '10MAR1889'}, 'F5': {'HUSB': 'I1', 'WIFE': 'NA', 'CHIL': ['I5', 'I6', 'I7'], 'MARR': 'NA', 'DIV': 'NA'}, 'F6': {'HUSB': 'NA', 'WIFE': 'I2', 'CHIL': ['I8', 'I9', 'I10'], 'MARR': 'NA', 'DIV': 'NA'}, 'F7': {'HUSB': 'I5', 'WIFE': 'NA', 'CHIL': ['I11'], 'MARR': 'NA', 'DIV': 'NA'}, 'F8': {'HUSB': 'I13', 'WIFE': 'I14', 'CHIL': [], 'MARR': '10MAR2013', 'DIV': '1JAN1980'}}

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

    def testUS06_CheckDivorceBeforeDeath(self):
        print()
        print("Testing US06_divorceBeforeDeath:")

        assert divorceBeforeDeath("F1", self.date1, self.date2, self.date2) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.date2

        assert divorceBeforeDeath("F1", self.date1, self.date2, self.emptyDate) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.emptyDate

        assert divorceBeforeDeath("F1", self.date1, self.emptyDate, self.date2) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date2

        assert divorceBeforeDeath("F1", self.date1, self.emptyDate, self.emptyDate) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.emptyDate

        # Negative cases

        # assert divorceBeforeDeath("F1", self.date2, self.date1, self.date2) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.date2

        # assert divorceBeforeDeath("F1", self.date2, self.date1, self.emptyDate) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.emptyDate

        # assert divorceBeforeDeath("F1", self.date2, self.emptyDate, self.date1) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date1

    def testUS12_CheckParentsTooOld(self):
        print()
        print("Testing US12_parentChildAgeCheck:")
        #self.date3 = ("10MAR1889")
        #self.date4 = ("10MAR1899")
        #self.date5 = ("10MAR1920")

        assert parentChildAgeCheck("F1", self.date1, self.date5, self.date5) == True, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date5
        
        assert parentChildAgeCheck("F1", self.date1, self.date5, self.date4) == False, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date4
        
        assert parentChildAgeCheck("F1", self.date2, self.date3, self.date5) == False, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date5
        
        assert parentChildAgeCheck("F1", self.date2, self.date3, self.date4) == False, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date4
       
        #Negative Cases
        # mother 61 years older
        # assert parentChildAgeCheck("F1", self.date1, self.date5, self.date4) == True, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date4
        # father 81 years older
        # assert parentChildAgeCheck("F1", self.date2, self.date3, self.date5) == True, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date5
        # both too old 
        # assert parentChildAgeCheck("F1", self.date2, self.date3, self.date4) == True, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date4


    def testUS14_CheckMultipleBirths(self):
        # test case to check if multiple births have the same birthday
        
        for key, value in self.familiesTest.items():
           childList = self.familiesTest[key]["CHIL"]
           self.assertTrue(CheckMultipleBirths(childList))
           #self.assertFalse(CheckMultipleBirths(childList))
    
    def testUS16_CheckSameLastNameAsFather(self):
        # Test case to check if the last name of child, is same as father
        
       for key, value in self.familiesTest.items():
           childList = self.familiesTest[key]["CHIL"]
           #self.assertTrue(CheckSameLastNameAsFather(childList))

    def testUniqueIDUS22(self):
        # test case to check IndividualID is unique.
        self.assertFalse(uniqueIDCheck('I1', individuals))

        # test case to check FamilyID is unique.
        self.assertFalse(uniqueIDCheck('F1', families))


    def testRead(self):
        # test if read is correct
        path = "./My-Family-18-May-2017-411.ged"
        individuals, families = readFile(path)
        self.assertEqual(self.individualsTest, individuals) 
        self.assertEqual(self.familiesTest, families)     

    # def testUniqueFamilyUS24(self):
    #     # test case to check IndividualID is unique.
    #     assert uniqueIDCheck('I1', individuals) == False

    #     # test case to check IndividualID is unique.
    #     assert uniqueIDCheck('I1', individuals) == False                



if __name__ == "__main__":

	# run all tests
    unittest.main() 

# End of File
